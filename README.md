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

1. Navigate to the root directory:

   ```bash
   cd ticket-system
   ```
2. Create a virtual environment:
    ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
    ```bash
    source env/bin/activate
   ```


4. Install backend dependencies:

   ```bash
    pip install -r requirements.txt
   ```

5. Install frontend dependencies:

   ```bash
   cd client
   npm install
   ```
6. Navigate to the project directory
    ```bash
   cd ..
   ```

7. Run the web application:

   ```bash
   honcho start -f Procfile.dev
   ```
## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).


## Usage

- Register a new user account or log in with existing credentials.
- Navigate to the ticket management section to create, view, update, or delete tickets.
- Log out when done.

