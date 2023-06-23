from scripts.helpful_scripts import get_account
from brownie import FundMe

latestContract = FundMe[-1]
account = get_account()

def fund():
    entranceFee = latestContract.getEntranceFee()
    print(f'Current entry fee {entranceFee}')
    print('Funding...')
    latestContract.fund({'from':account, 'value':entranceFee})
    print('Funded!')

def withdraw():
    latestContract.withdraw({'from':account})

def main():
    fund()
    withdraw()