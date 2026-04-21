from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _coincheck_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_coincheck.exchange_data import CoincheckExchangeDataSpot
from bt_api_coincheck.feeds.live_coincheck.spot import CoincheckRequestDataSpot


def register_coincheck(registry: ExchangeRegistry | type[ExchangeRegistry]) -> None:
    registry.register_feed("COINCHECK___SPOT", CoincheckRequestDataSpot)
    registry.register_exchange_data("COINCHECK___SPOT", CoincheckExchangeDataSpot)
    registry.register_balance_handler("COINCHECK___SPOT", _coincheck_balance_handler)


def register(registry: ExchangeRegistry | type[ExchangeRegistry] | None = None) -> None:
    target = ExchangeRegistry if registry is None else registry
    register_coincheck(target)
