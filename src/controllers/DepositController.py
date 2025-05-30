from flask import Blueprint, request, jsonify

# Models
from src.models.Deposits import Deposit, DepositsSchema
# Security
from src.utils.Security import Security
# Services
from src.services.DepositService import DepositService

deposit_schema = DepositsSchema()
deposits_schema = DepositsSchema(many=True)

main = Blueprint('deposit_blueprint', __name__)

@main.route('/<account_number>', methods=['GET'])
def account_deposits_controller(account_number):
    has_access = Security.verify_token(request.headers)

    if has_access:
        page = request.args.get('page', default=1, type=int)
        limit = request.args.get('limit', default=10, type=int)
        
        _deposit = Deposit(account=account_number)
        deposits, total = DepositService.account_deposits_service(_deposit, page, limit)
        return jsonify({
                'deposits': deposits_schema.dump(deposits),
                'pagination': {
                    'page': page,
                    'limit': limit,
                    'total': total
                }
        }), 200
    else:
        return jsonify({'message': '¡Error de autenticación, inicie sesión!'}), 401

@main.route('/<account_number>', methods=['POST'])
def deposit_controller(account_number):
    has_access = Security.verify_token(request.headers)

    if has_access:
        amount = request.json['amount']
        _deposit = Deposit(account=account_number, amount=amount)
        message = DepositService.deposit_service(_deposit)

        if message == 'Depósito realizado con éxito.':
            return jsonify({'message': message }), 200
        else:
            return jsonify({'message': message}), 400
    else:
        return jsonify({'message': '¡Error de autenticación, inicie sesión!'}), 401    
