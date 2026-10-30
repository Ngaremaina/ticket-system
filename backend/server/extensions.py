from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Extensions are created here unbound and attached to the app in create_app()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
mail = Mail()
cors = CORS()
