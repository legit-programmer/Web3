from solcx import compile_standard, install_solc
import json
from web3 import Web3
import dotenv
import os

dotenv.load_dotenv()

# Deployment menu

install_solc('0.8.8')
os.chdir('../contracts')
files = os.listdir()
mainFile = ''
for i in files:
    if '.sol' in i:
        print(f'{files.index(i)} {i}')

mainFile = files[int(input('enter: '))]
fileName = mainFile[:-4]

#Compiling .sol file
print('Compiling...')
with open(f"{os.path.join(mainFile)}", "r") as file:
    simple_storage_file = file.read()

    compiledSol = compile_standard(
        {"language": "Solidity",
         "sources": {f"{mainFile}": {"content": simple_storage_file}},
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
print('Compiled!')
#Storing compiled bytecode

with open("../scripts/compiled.json", 'w') as file:
    json.dump(compiledSol, file)

byteCode = compiledSol["contracts"][mainFile][fileName]["evm"]["bytecode"]["object"]
abi = compiledSol['contracts'][mainFile][fileName]['abi']
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/8dBj1dorpFTrm_5bWnKdvESink68H7KV'))

myAddress = '0x7F271cb4EeA76990c8B3aFDB882F3e0751C9676A'
gasPrice = web3.eth.gas_price
# Fake development keys
privateKey = os.getenv("PRIVATE_KEY")

#Deploying contract

print('Deploying...')
SimpleStorage = web3.eth.contract(abi=abi, bytecode=byteCode)
nonce = web3.eth.get_transaction_count(myAddress)
transaction = SimpleStorage.constructor().build_transaction(
    {"from": myAddress, "nonce": nonce})
signed = web3.eth.account.sign_transaction(transaction, privateKey)
txHash = web3.eth.send_raw_transaction(signed.rawTransaction)
txReciept = web3.eth.wait_for_transaction_receipt(txHash)
print(f'Balance {web3.eth.get_balance(myAddress)}')

print("Contract Deployed!")



