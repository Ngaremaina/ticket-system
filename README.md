# Ticket System

This is a ticket system application that allows admins to perform CRUD (Create, Read, Update, Delete) operations on tickets and provides authentication for all users. The customers have the option to browse through the available events and acquire tickets for the specific event they wish to attend, whether it be VIP or Regular. The backend is built using Flask, a micro web framework for Python, while the frontend is built using React, a JavaScript library for building user interfaces.

## Features

- User authentication: All users can sign up, log in, and log out.
- Ticket management: Admins can create, view, update, and delete tickets and clients can view and book tickets.

## Technologies Used

- Backend:
  - Flask: Micro web framework for Python.
  - Flask-RESTful: Extension for creating REST APIs with Flask.
  - SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.

- Frontend:
  - React: JavaScript library for building user interfaces.
  - React Router: Declarative routing for React.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ngaremaina/ticket-system
   ```

2. Install backend dependencies:

   ```bash
   cd ticket-system/backend
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Set environment variables:

   Create a `.env` file in the `backend` directory with the following contents:

   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

5. Run the backend server:

   ```bash
   export FLASK_APP=main.py
   flask run
   ```

6. Install frontend dependencies:

   ```bash
   cd ../frontend
   npm install
   ```

7. Run the frontend server:

   ```bash
   npm start
   ```

## Usage

- Register a new user account or log in with existing credentials.
- Navigate to the ticket management section to create, view, update, or delete tickets.
- Log out when done.
