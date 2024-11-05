from flask import Blueprint, request, jsonify, current_app
from server.db import get_db

lottery_numbers_bp = Blueprint('lottery_numbers', __name__)

@lottery_numbers_bp.route('/lottery', methods=['GET'])
def get_lottery_numbers():
    with current_app.app_context():
        db = get_db()
        lottery_numbers = db.execute('SELECT * FROM lottery_numbers').fetchall()
        lottery_numbers = [
        {
            "id": row[0],
            "number": row[1],
            "draw_date": row[2]
        }
        for row in lottery_numbers
    ]
    return jsonify(lottery_numbers)

""" @lottery_numbers_bp.route('/lottery_numbers', methods=['POST'])
def add_lottery_number():
    data = request.get_json()
    new_lottery_number = LotteryNumber(
        number=data['number'],
        draw_date=data['draw_date']
    )
    db.session.add(new_lottery_number)
    db.session.commit()
    return jsonify(new_lottery_number.to_dict()), 201

@lottery_numbers_bp.route('/lottery_numbers/<int:id>', methods=['DELETE'])
def delete_lottery_number(id):
    lottery_number = LotteryNumber.query.get_or_404(id)
    db.session.delete(lottery_number)
    db.session.commit()
    return '', 204 """
