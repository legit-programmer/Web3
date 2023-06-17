from solcx import compile_standard, install_solc
import json
from web3 import Web3
import dotenv
import os

dotenv.load_dotenv()

install_solc('0.8.8')
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

    compiledSol = compile_standard(
        {"language": "Solidity",
         "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
         "settings": {
             "outputSelection": {
                 "*": {
                     "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                 }
             }
         },

         },
        solc_version="0.8.8"
    )

with open("compiled.json", 'w') as file:
    json.dump(compiledSol, file)

byteCode = compiledSol["contracts"]["SimpleStorage.sol"]['SimpleStorage']["evm"]["bytecode"]["object"]
abi = compiledSol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
chainid = 1337
myAddress = '0x375Ba847f5Abc256ccE68c1150BD930dA91A2Df0'
# Fake development keys
privateKey = os.getenv("PRIVATE_KEY")

SimpleStorage = web3.eth.contract(abi=abi, bytecode=byteCode)
nonce = web3.eth.get_transaction_count(myAddress)
transaction = SimpleStorage.constructor().build_transaction(
    {"chainId": chainid, "from": myAddress, "nonce": nonce})
signed = web3.eth.account.sign_transaction(transaction, privateKey)
txHash = web3.eth.send_raw_transaction(signed.rawTransaction)
print(signed)
