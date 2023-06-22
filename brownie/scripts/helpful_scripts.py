from brownie import network, accounts, MockV3Aggregator
import web3
import os

def get_account():
    if network.show_active()=='development':
        return accounts[0]
    else:
        return accounts.add(os.getenv('PRIVATE_KEY'))
    
def deploy_mocks():
    print('Deploying Mocks...')
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(18, web3.Web3.toWei(1000, 'ether'), {'from':get_account()})
    print('Mocks deployed')
    return MockV3Aggregator[-1].address