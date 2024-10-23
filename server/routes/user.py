from flask import Blueprint, jsonify
from server.db import get_db

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users', methods=['GET'])
def check_users():
    db = get_db()
    users = db.execute('SELECT * FROM user').fetchall()
    if users:
        return jsonify({
            'status': 'success',
            'message': f"{len(users)} users found.",
            'users': [dict(user) for user in users]
        }), 200
    else:
        return jsonify({
            'status': 'success',
            'message': "No users found."
        }), 200