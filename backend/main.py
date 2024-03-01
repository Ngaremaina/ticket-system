from server import app, authentication
from werkzeug.serving import run_simple

if __name__ == "__main__":
    run_simple(
        hostname='0.0.0.0',
        port=5000,
        application=app
    )