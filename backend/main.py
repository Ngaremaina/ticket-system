import os

from server import create_app

# WSGI entry point used by gunicorn (main:app) and the flask CLI
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
