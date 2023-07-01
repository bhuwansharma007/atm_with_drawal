# from main import APP

from fastapi import APIRouter
from api.controllers import withdrawal_operation


internal = APIRouter( prefix = "/internal", tags = ['transaction'])


@internal.route('/withdraw')
class Withdraw:
    """Handles the request related to withdrawing the amount"""
    def post(self,request):
        return withdrawal_operation(request)





