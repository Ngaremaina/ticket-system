import os

from dotenv import load_dotenv

# Load variables from backend/.env so gunicorn and the flask CLI see the same config
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


def _bool(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")


def _database_url():
    url = os.environ.get("DATABASE_URL", "")
    # Neon / Heroku style URLs use the "postgres://" scheme which SQLAlchemy no longer accepts
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = _database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Neon suspends idle computes and closes idle connections, so check
    # connections before use and recycle them before the server drops them.
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "pool_size": int(os.environ.get("DB_POOL_SIZE", 5)),
        "max_overflow": int(os.environ.get("DB_MAX_OVERFLOW", 5)),
    }

    # Comma separated list of frontend origins allowed to call the API
    CORS_ORIGINS = [
        origin.strip()
        for origin in os.environ.get(
            "CORS_ORIGINS", "http://localhost:3000,http://localhost:4000"
        ).split(",")
        if origin.strip()
    ]

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = _bool("SESSION_COOKIE_SECURE", False)
    # Use "None" (with SESSION_COOKIE_SECURE=true) when the frontends are on a different domain
    SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE", "Lax")

    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = _bool("MAIL_USE_TLS", True)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", MAIL_USERNAME)


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = Config.SECRET_KEY or "dev-only-insecure-secret"
    SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI or "sqlite:///app.db"


class ProductionConfig(Config):
    SESSION_COOKIE_SECURE = _bool("SESSION_COOKIE_SECURE", True)


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "test-secret"
    # CI can point this at a real Postgres service; locally it falls back to in-memory SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL", "sqlite://")
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    BCRYPT_LOG_ROUNDS = 4
    MAIL_SUPPRESS_SEND = True


CONFIGS = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
