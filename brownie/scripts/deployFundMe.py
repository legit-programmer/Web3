from brownie import accounts, FundMe, network
from.helpful_scripts import get_account

def deploy():
    account = get_account()
    FundMe.deploy('0x694AA1769357215DE4FAC081bf1f309aDC325306', {'from':account}, publish_source=True)
    
def main():
    network.priority_fee('1.5 gwei')
    deploy()