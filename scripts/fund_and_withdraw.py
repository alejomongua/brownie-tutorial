from brownie import FundMe
from scripts.helpers import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    fund_me.fund({'from': account, 'value': entrance_fee})
    print(f"Contract funded with {entrance_fee}")
    # total_funded = fund_me.addressToAmountFunded()[account]
    # print(f'Total funded by me: {total_funded}')


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({'from': account})
    print(f'All funds have been withdrawn')


def main():
    fund()
    withdraw()
