from server import *

@app.route("/register", methods = ["POST"])
def add_users():
    email = request.json["email"]
    password = request.json["password"]
    role = request.json["role"]

    user_exists = Auth.query.filter_by(email = email).first()

    if user_exists:
        return jsonify(message = "User exists")

    hashed_password = bcrypt.generate_password_hash(password)

    new_user = Auth(email = email, password = hashed_password, role = role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id":new_user.id,
        "email":new_user.email
    })

@app.route("/login", methods = ["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = Auth.query.filter_by(email = email).first()

    session["user_id"] = user.id
    

    if user is None:
        return jsonify(message = "Unauthorized")

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify(message = "Unauthorized")
      
    return jsonify({
        "id":user.id,
        "email": email,
        "role": user.role
       
    })


@app.route("/current_user", methods=["GET"])
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify(error =  "Unauthorized")

    user = Auth.query.filter_by(id = user_id).first()
    response = jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role
    })

    return response



@app.route("/logout", methods = ["POST"])
def logout_user():
    if "user_id" in session:
        session.pop("user_id")

    return make_response(jsonify("logged out"), 200)


