from brownie import network, accounts
import os

def get_account():
    if network.show_active()=='development':
        return accounts[0]
    else:
        return accounts.add(os.getenv('PRIVATE_KEY'))