from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bcrypt import Bcrypt


import secrets
from flask_cors import CORS

import secrets
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


app.config['SECRET_KEY'] = secrets.token_hex(16)

# Db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskreact'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'created_at': user.created_at} for
        user in users
    ]
    return jsonify({'users': users_list})

@app.route('/create', methods=['POST'])
def store():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({'error': 'Name, email, and password are required'}), 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': 'Successfully created user',
            'user': {
                'id': new_user.id,
                'name': new_user.name,
                'email': new_user.email
            }
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/show/user/<int:id>', methods=['GET'])
def show(id):
    user = User.query.get(id)

    if user:
        return jsonify({
            'message': 'Details for the user',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password
            }
        }), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')


    user.name = name
    user.email = email
    user.password = hashed_password

    db.session.commit()

    return jsonify({
        'message': 'User updated successfully',
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
    }), 200



@app.route('/delete/<id>', methods = ['DELETE'])
def destroy(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return jsonify({
        'message': 'User deleted succesfully',
        'user': ''
    }), 200



if __name__ == '__main__':
    app.run(debug=True)

