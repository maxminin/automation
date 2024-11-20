# import ast
# import json
#
# from web3 import Web3
#
# from routers import config
#
#
# def get_balance_for_token(token_symbol: str, data: dict):
#     w3 = Web3(Web3.HTTPProvider(data['rpc_url']))
#     if not w3.is_connected():
#         raise Exception("Didn't connect to w3")
#     token_address = config.TOKEN_MAPPERS[token_symbol]
#     token_contract = w3.eth.contract(
#             address=Web3.to_checksum_address(token_address),
#             abi=json.load(open("abi's/abi1.json"))
#         )
#     func = data['function_name']
#     method = getattr(token_contract.functions, func)
#     args = ast.literal_eval(data['args'])
#     return method(*args)
