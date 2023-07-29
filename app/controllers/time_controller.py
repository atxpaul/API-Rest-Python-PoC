from flask import Blueprint, jsonify
from app.services.time_service import get_current_time

time_bp = Blueprint('time', __name__)


@time_bp.route('/time', methods=['GET'])
def get_time():
    current_time_model = get_current_time()
    return jsonify(current_time_model.to_dict())
