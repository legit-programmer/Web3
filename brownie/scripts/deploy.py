from brownie import accounts, SimpleStorage, network, config
import os

def get_account():
    if network.show_active()=='development':
        return accounts[0]
    else:
        return accounts.add(os.getenv('PRIVATE_KEY'))

def deploy_simple_storage():
    account = get_account()
    SimpleStorage.deploy({"from":account})
    # number of blocks to wait for confirmation transaction.wait(1)

def main():
    # account = accounts.add(os.getenv('PRIVATE_KEY'))
    # print(account)
    network.priority_fee("1.5 gwei")
    deploy_simple_storage()