from brownie import MyFirstContract, config, accounts

def deployContract():
    account = accounts.add(config["wallets"]["from_key"])
    MyFirstContract.deploy({'from': account})

def main():
    deployContract()