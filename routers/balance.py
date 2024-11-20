import json

from web3 import Web3
from fastapi import APIRouter


balance_router = APIRouter()


@balance_router.post('/huy')
def get_balance_for_token(data: dict):
    w3 = Web3(Web3.HTTPProvider(data['rpc_url']))
    if not w3.is_connected():
        raise Exception("Didn't connect to w3")
    token_address = data['token_address']
    token_contract = w3.eth.contract(
            address=Web3.to_checksum_address(token_address),
            abi=json.load(open("abi's/abi1.json"))
        )
    func = data['function_name']
    method = getattr(token_contract.functions, func)
    args = tuple(data['args'])
    try:
        a = method(*args).call()
        return a
    except Exception as e:
        return {"error": str(e)}




