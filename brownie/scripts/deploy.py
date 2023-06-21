from brownie import accounts, SimpleStorage, network, config
import os
from.helpful_scripts import get_account



def deploy_simple_storage():
    account = get_account()
    SimpleStorage.deploy({"from":account})
    # number of blocks to wait for confirmation transaction.wait(1)

def main():
    # account = accounts.add(os.getenv('PRIVATE_KEY'))
    # print(account)
    network.priority_fee("1.5 gwei")
    deploy_simple_storage()