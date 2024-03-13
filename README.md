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
2. Navigate to the root directory:

   ```bash
   cd ticket-system
   ```
3. Create a virtual environment:
    ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
    ```bash
    source env/bin/activate
   ```
    
5. Install backend dependencies:

   ```bash
    pip install -r requirements.txt
   ```
6. Navigate to the flask init file in the server directory:
   ```bash
   cd backend/server/
   ```

7. In the file, change the mysql url to your own mysql:
   ```bash
   app.config["SQLALCHEMY_DATABASE_URI"] = mysql+pymysql://username:password@localhost/databasename
   ```
8. Navigate to the backend directory:
   ```bash
   cd ..
   ```
9. Run the following commands to migrate the models into the database:
   ```bash
   export FLASK_APP=main.py
   flask db upgrade head
   ```
10. Navigate to the frontend directories and install frontend dependencies:

     ```bash
       cd client
       npm install
     ```
     ```bash
       cd ../admin
       npm install
     ```
11. Navigate to the project directory
     ```bash
       cd ..
     ```
12. Run the web application:
     ```bash
     honcho start -f Procfile.dev
     ```
     
## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).

## Usage

- Register a new user account or log in with existing credentials.
- Navigate to the ticket management section to create, view, update, or delete tickets.
- Log out when done.

