from brownie import SimpleStorage, accounts


# brownie test -k function name: will only test given function
# brownie test -s: more robust and will include print statements

def test_deploy():
    #Testing categories:
    #Arrange
    #Acting
    #Assert

    #arrange
    account = accounts[0]

    #act
    simple_storage = SimpleStorage.deploy({'from':account})
    starting_value = simple_storage.retrieve()
    expected = 0

    #assert
    assert starting_value==expected 

def test_update_storage():
    #arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from':account})

    #act
    transaction = simple_storage.storeNumber(9, {'from':account})
    transaction.wait(1)
    starting_value = simple_storage.retrieve()
    expected_value = 9

    #assert
    assert starting_value==expected_value