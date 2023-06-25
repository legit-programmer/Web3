from web3 import Web3
from brownie import FundMe, network, config
from .helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy():
    print(f'Active network is {network.show_active()}')
    network.priority_fee('1.5 gwei')
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress = config['networks'][network.show_active(
        )]['priceFeed']
    else:

        priceFeedAddress = deploy_mocks()

    account = get_account()
    return FundMe.deploy(priceFeedAddress, {'from': account})


def main():
    
    deploy()
