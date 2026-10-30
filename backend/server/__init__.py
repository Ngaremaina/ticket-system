import logging
import os

import click
from flask import Flask, jsonify
from marshmallow import ValidationError
from sqlalchemy import text
from werkzeug.exceptions import HTTPException

from server.config import CONFIGS
from server.extensions import bcrypt, cors, db, mail, migrate


def create_app(config_name=None):
    """Application factory: build and configure a Flask app instance."""
    config_name = config_name or os.environ.get("FLASK_ENV", "production")
    app = Flask(__name__)
    app.config.from_object(CONFIGS[config_name])

    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY must be set")
    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        raise RuntimeError("DATABASE_URL must be set (e.g. your Neon connection string)")

    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)
    cors.init_app(app, origins=app.config["CORS_ORIGINS"], supports_credentials=True)

    # Import models so they are registered with SQLAlchemy / Alembic
    from server import models  # noqa: F401
    from server.authentication import auth
    from server.routes.events import events
    from server.routes.tickets import tickets
    from server.routes.type import types
    from server.routes.user import user

    for blueprint in (auth, events, tickets, types, user):
        app.register_blueprint(blueprint)

    register_error_handlers(app)
    register_commands(app)

    # Health check used by load balancers / uptime monitors
    @app.get("/health")
    def health():
        try:
            db.session.execute(text("SELECT 1"))
        except Exception:
            app.logger.exception("Database health check failed")
            return jsonify(status="error", database="unreachable"), 503
        return jsonify(status="ok", database="ok"), 200

    return app


def register_error_handlers(app):
    # Return JSON instead of HTML error pages
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        db.session.rollback()
        return jsonify(error="Validation failed", details=error.messages), 400

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify(error=error.description), error.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        db.session.rollback()
        app.logger.exception("Unhandled error")
        return jsonify(error="Internal server error"), 500


def register_commands(app):
    @app.cli.command("create-admin")
    @click.argument("email")
    @click.password_option()
    def create_admin(email, password):
        """Create an admin user (admins cannot self-register through the API)."""
        from server.models import Auth

        if Auth.query.filter_by(email=email).first():
            raise click.ClickException("A user with that email already exists")
        admin = Auth(
            email=email,
            password=bcrypt.generate_password_hash(password).decode("utf-8"),
            role="admin",
        )
        db.session.add(admin)
        db.session.commit()
        click.echo(f"Admin {email} created")
