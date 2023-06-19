from brownie import accounts, SimpleStorage
import os

def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    transaction = simple_storage.storeNumber(9, {"from":account})
    transaction.wait(1)# number of blocks to wait for
    print(simple_storage.retrieve())

def main():
    # account = accounts.add(os.getenv('PRIVATE_KEY'))
    # print(account)
    deploy_simple_storage()