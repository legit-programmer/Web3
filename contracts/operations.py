from deploy import *
from web3 import Web3

#working with contract
#prerequisites 1. contract address 2. Contract ABI
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
contract = web3.eth.contract(address=txReciept.contractAddress, abi=abi)
# print(contract.functions.storeNumber(15).call())
# print(contract.functions.retrieve().call())

storeTx = contract.functions.storeNumber(20).build_transaction(
    {'chainId':chainid, 'from':myAddress, 'nonce':nonce+1}
)
signed = web3.eth.account.sign_transaction(storeTx, privateKey)
transHash = web3.eth.send_raw_transaction(signed.rawTransaction)

print(contract.functions.retrieve().call())