# Ticket System

This is a ticket system application that allows admins to perform CRUD (Create, Read, Update, Delete) operations on tickets and provides authentication for all users. The customers have the option to browse through the available events and acquire tickets for the specific event they wish to attend, whether it be VIP or Regular. The backend is built using Flask, a micro web framework for Python, while the frontend is built using React, a JavaScript library for building user interfaces.

## Features

- User authentication: All users can sign up, log in, and log out.
- Ticket management: Admins can create, view, update, and delete tickets and clients can view and book tickets.
- Health check endpoint and JSON error responses for production monitoring.

## Technologies Used

- Backend: Flask, SQLAlchemy, Flask-Migrate (Alembic), marshmallow, gunicorn
- Database: [Neon](https://neon.tech) serverless Postgres (SQLite fallback for local dev)
- Frontend: React, React Router, Tailwind CSS (two apps: `client` and `admin`)
- CI: GitHub Actions (Python, Node, CodeQL, Dependabot auto-merge)

## Project Structure

```
backend/   Flask API (app factory in server/__init__.py, config in server/config.py)
client/    Customer React app (port 3000)
admin/     Admin React app (port 4000)
```

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Ngaremaina/ticket-system
   cd ticket-system
   ```

2. Create the backend virtual environment and install dependencies:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   ```

3. Configure the environment:
   ```bash
   cp .env.example .env
   ```
   Then edit `backend/.env` — at minimum set `SECRET_KEY` and `DATABASE_URL` (see [Connecting to Neon](#connecting-to-neon)).
   If `DATABASE_URL` is left empty in development, a local SQLite file is used.

4. Apply migrations and create an admin account:
   ```bash
   flask db upgrade
   flask create-admin admin@example.com
   ```
   Admins cannot sign up through the API; public `/register` always creates `client` users.

5. Install frontend dependencies:
   ```bash
   cd ../client && npm install
   cd ../admin && npm install
   cd ..
   ```

6. Run everything:
   ```bash
   backend/.venv/bin/honcho start -f Procfile.dev
   ```

## Connecting to Neon

1. Create a project at [console.neon.tech](https://console.neon.tech).
2. Open **Connect**, enable **Connection pooling**, and copy the connection string. It looks like:
   ```
   postgresql://USER:PASSWORD@ep-xxxx-pooler.REGION.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   ```
3. Put it in `backend/.env` as `DATABASE_URL` (or in your host's environment variables in production).
4. Run `flask db upgrade` from `backend/` to create the tables.
5. Check the connection: `curl http://localhost:5000/health` should return `{"database": "ok", "status": "ok"}`.

The engine uses `pool_pre_ping` and recycles connections every 5 minutes, so the app recovers
cleanly when Neon suspends an idle compute.

## Testing

```bash
# Backend (uses in-memory SQLite; set TEST_DATABASE_URL to run against Postgres)
cd backend && pytest
ruff check .

# Frontends
cd client && CI=true npm test
cd admin && CI=true npm test
```

## Deployment

- **Backend:** the root `Procfile` runs `flask db upgrade` on release and serves the API with gunicorn.
  Set `FLASK_ENV=production`, `SECRET_KEY`, `DATABASE_URL`, and `CORS_ORIGINS` (your frontend URLs).
  If the frontends are on a different domain than the API, also set `SESSION_COOKIE_SAMESITE=None`.
- **Frontends:** build with `REACT_APP_API_URL=https://your-api.example.com npm run build` and serve the `build/` folder.
- `GET /health` reports API and database status for uptime checks.

## CI/CD

| Workflow | What it does |
| --- | --- |
| `python.yml` | Ruff lint, runs Alembic migrations up/down, and runs pytest against a Postgres 17 service |
| `node.yml` | Tests and builds `admin` and `client` |
| `codeql.yml` | Security scanning for Python and JavaScript |
| `automerge.yml` | Approves and auto-merges Dependabot patch/minor updates once required checks pass |

For auto-merge to work, enable **Settings → General → Allow auto-merge** and add a branch
protection rule on `main` that requires the `Lint & test (Postgres)`, `admin` and `client` checks.

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).

## Usage

- Register a new user account or log in with existing credentials.
- Navigate to the ticket management section to create, view, update, or delete tickets.
- Log out when done.

