import pytest
from brownie import FundMe, network, accounts, exceptions
from scripts.helpers import LOCAL_BLOCKCHAINS_ENVIRONMENTS, get_account
from scripts.deploy import deploy


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({
        'from': account,
        'value': entrance_fee,
    })
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx = fund_me.withdraw({'from': account})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAINS_ENVIRONMENTS:
        pytest.skip('only for local testing')
        return
    fund_me = deploy()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({'from': bad_actor})
