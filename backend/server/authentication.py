from server import *

#Register user 
@app.route("/register", methods = ["POST"])
def add_users():

    #Get the details from the user
    email = request.json["email"]
    password = request.json["password"]
    role = request.json["role"]

    #Check whether the user is in the database
    user_exists = Auth.query.filter_by(email = email).first()

    #If the user exists return the message user exists
    if user_exists:
        return jsonify(message = "User exists")
    
    #Hash the password using generate_password_hash() function
    hashed_password = bcrypt.generate_password_hash(password)

    #Add user to the Auth model
    new_user = Auth(email = email, password = hashed_password, role = role)

    #Add user to the database
    db.session.add(new_user)
    db.session.commit()

    #Return the user details
    return jsonify({
        "id":new_user.id,
        "email":new_user.email
    })


#Route for login user
@app.route("/login", methods = ["POST"])
def login_user():
    #Get the details from the user
    email = request.json["email"]
    password = request.json["password"]

    #Check whether the user is in the database
    user = Auth.query.filter_by(email = email).first()

    #Create a session to store the user id
    session["user_id"] = user.id
    
    #If the user does not exist return the message unauthorized
    if user is None:
        return jsonify(message = "Unauthorized")
    
    #If the password is wrong return the message unauthorized
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify(message = "Unauthorized")
    
    #Return the user details
    return jsonify({
        "id":user.id,
        "email": email,
        "role": user.role
       
    })

#Get details of the logged in user
@app.route("/current_user", methods=["GET"])
def get_current_user():
    #Get the stored session by id
    user_id = session.get("user_id")

    #If invalid return the error message unauthorized
    if not user_id:
        return jsonify(error =  "Unauthorized")
    
    #Query the database and find the user by id
    user = Auth.query.filter_by(id = user_id).first()

    #Return the user details
    response = jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role
    })

    return response


#Route for logout
@app.route("/logout", methods = ["POST"])
def logout_user():
    #Check if user is in session
    if "user_id" in session:
        #If true remove the id from the session
        session.pop("user_id")
        
    #Return the message logged out 
    return make_response(jsonify("logged out"), 200)


