from brownie import accounts, FundMe, network
from.helpful_scripts import get_account

def deploy():
    account = get_account()
    FundMe.deploy({'from':account})
    
def main():
    network.priority_fee('1.5 gwei')
    deploy()