from brownie import ERC20Basic, config, accounts, network

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = ERC20Basic[-1]
    print("Total Supply is", erc20.totalSupply({'from': account}))

    tx = erc20.transfer('0x0BA3e9178C1459DcF70C64C17740fBF81425063f',10,{'from': account})
    tx.wait(1)
    print("New token balance is", erc20.balanceOf(account.address,{'from': account}))
