from flask import Flask, jsonify, request, Blueprint
from models.user import UserModel  # Import your UserModel from models
from app import db, app
import random, string, datetime, jwt

userBP = Blueprint('userBP', __name__)


@userBP.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    # Assuming you want to retrieve a user with a specific ID
    user = UserModel.query.get(id)
    if user:
        return jsonify({"message": "success", "user_id": user.id, "name": user.username, "email": user.email})
    else:
        return jsonify({"message": "User not found"}), 404
    

def makeID():
    # create a 16 character long string of random letters (lowercase & uppercase) and digits
    id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
    return id


@userBP.route('/user/<username>/<email>', methods=['POST'])
def create_user(username, email):
    print(username,email)

    # generate a random 16 character long string of letters and digits
    id = makeID()
    print(id)

    if not id or not username or not email:
        return jsonify({"message": "Missing required fields"}), 400

    newUser = UserModel(id=id, username=username, email=email)

    # Assuming you have a database session called db_session to add and commit the user
    db.session.add(newUser)
    db.session.commit()

    print("HERE")

    return jsonify({"message": "User Created Successfully", "user_id": newUser.id, "name": newUser.username, "email": newUser.email}), 201


# Token generation function
def generate_token(username):
    payload = {
        'sub': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expiration time
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token


#make a login functoin that uses a token-based authentication system
@userBP.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    #check if username and password are correct
    user = UserModel.query.filter_by(username=username).first()
    if user and user.password == password:
        token = generate_token(username)
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Authentication failed'}), 401
    
# Protected route
# API Endpoints: In a RESTful API, the /protected route might represent a specific API endpoint 
# that provides access to a resource. For instance, it could be used to retrieve a list of user-specific items, 
# create new items, update existing ones, or perform other CRUD (Create, Read, Update, Delete) operations.
### IN this program, this can be used to access the user's information
@userBP.route('/protected', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': 'Welcome, {}'.format(payload['sub'])})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
