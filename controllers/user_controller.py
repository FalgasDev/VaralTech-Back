from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from errors import EmptyStringError, AuthError
from models.user_model import register, login, User
from models.otp_model import verify_otp

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.json
    try:
        register(data)
        return jsonify({'status': 'Usuário cadastrado com sucesso!'}), 201
    except (KeyError, EmptyStringError, AuthError) as e:
        return jsonify({'error': e.message if hasattr(e, 'message') else str(e)}), 400


@user_blueprint.route('/login', methods=['POST'])
def login_user():
    data = request.json
    try:
        result = login(data)
        # result tem: otp_code, email, name
        # O front usa esses dados para enviar o email via EmailJS
        return jsonify(result), 200
    except (KeyError, EmptyStringError, AuthError) as e:
        return jsonify({'error': e.message if hasattr(e, 'message') else str(e)}), 400


@user_blueprint.route('/verify-otp', methods=['POST'])
def verify_otp_route():
    data = request.json
    try:
        result = verify_otp(data)
        # Só aqui o JWT é gerado e retornado
        return jsonify(result), 200
    except (KeyError, AuthError) as e:
        return jsonify({'error': e.message if hasattr(e, 'message') else str(e)}), 400


@user_blueprint.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'Usuário não encontrado.'}), 404

    return jsonify(user.to_dict()), 200
