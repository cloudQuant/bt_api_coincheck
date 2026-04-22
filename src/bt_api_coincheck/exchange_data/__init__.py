from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    "get_exchange_info": "GET /api/exchange_status",
    "get_tick": "GET /api/ticker",
    "get_depth": "GET /api/order_books",
    "get_kline": "GET /api/exchange/orders/rate",
    "get_trades": "GET /api/trades",
    "get_account": "GET /api/accounts",
    "get_balance": "GET /api/accounts/balance",
    "make_order": "POST /api/exchange/orders",
    "cancel_order": "DELETE /api/exchange/orders/{order_id}",
    "query_order": "GET /api/exchange/orders/transactions",
    "get_open_orders": "GET /api/exchange/orders/opens",
}


class CoincheckExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "coincheck"
        self.rest_url = "https://coincheck.com"
        self.wss_url = "wss://ws-api.coincheck.com"
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "4h": "4h",
            "1d": "1d",
            "1w": "1w",
        }
        self.legal_currency = ["JPY"]

    def get_symbol(self, symbol: str) -> str:
        return symbol.replace("-", "").replace("_", "")

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]


class CoincheckExchangeDataSpot(CoincheckExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
