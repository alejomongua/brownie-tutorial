from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpers import LOCAL_BLOCKCHAINS_ENVIRONMENTS, deploy_mocks, get_account


def deploy():
    """Deploys the contracat"""
    account = get_account()

    # publish_source=True requires environment variable ETHERSCAN_TOKEN

    # If we are on a persistent network like rinkeby, use associated
    # address, otherwise, deploy mocks
    if network.show_active() in LOCAL_BLOCKCHAINS_ENVIRONMENTS:
        print(f"The active network is {network.show_active()}")

        deploy_mocks()
        mock_v3_aggregator = MockV3Aggregator[-1]
        price_feed_address = mock_v3_aggregator.address
        publish_source = False

    else:
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_price_feed']
        publish_source = config['networks'][network.show_active(
        )]['publish_source']

    fund_me = FundMe.deploy(price_feed_address, {
                            'from': account}, publish_source=publish_source)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    """Gets called by brownie"""
    deploy()
