from brownie import MyFirstContract, config, accounts, network

def main():
    account = accounts.add(config["wallets"]["from_key"])
    myFirstContract = MyFirstContract[-1]
    tx = myFirstContract.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", myFirstContract.getNumber({'from': account}))
    print("adding 7 to number =", myFirstContract.addNumber(7,{'from': account}))
