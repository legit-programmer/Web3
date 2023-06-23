from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deployFundMe import deploy


def test_fund():
    #arrange
    deploy()
    latestContract = FundMe[-1]
    account = get_account()
    entrancefee = latestContract.getEntranceFee()
    #act
    tx = latestContract.fund({'from':account, 'value':entrancefee})
    tx.wait(1)
    expected_value = entrancefee
    #assert
    assert expected_value==latestContract.amounts(account.address)

def test_withdraw():
    #arrange
    latestContract = FundMe[-1]
    account = get_account()
    #act
    tx = latestContract.withdraw({'from':account})
    tx.wait(1)
    expected_value = 0
    #assert
    assert expected_value==latestContract.amounts(account.address)
    