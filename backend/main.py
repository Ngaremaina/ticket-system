from server import app, authentication
# import server.routes
from werkzeug.serving import run_simple

if __name__ == "__main__":
    run_simple(
        hostname='localhost',
        port=5000,
        application=app
    )