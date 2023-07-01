import json
from fastapi.encoders import jsonable_encoder
from util.base_class import ATM

def  withdrawal_operation(request):
    
    id = request['id']
    name = request['name']
    required_money = request['amount']
    
    # retriving account details and atm server
    with open("./users.json") as users_db:
        data = json.load(users_db)
    
    with open("./atm_server.json") as atm_db:
        available_denominations = json.load(atm_db)

    data = data['users']

    for user in data:
        if id in user['id']:
            atm_server = ATM(user['balance'],available_denominations)
            atm_server.validate_balance(required_money)
            atm_server.calculate_notes(required_money)
            atm_server.dispense_notes(required_money)
            atm_server.update_balance(required_money)


        




