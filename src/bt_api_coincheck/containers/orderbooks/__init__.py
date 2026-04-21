from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData


class CoincheckOrderBookData(OrderBookData):
    def __init__(
        self,
        order_book_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(order_book_info, has_been_json_encoded)
        self.exchange_name = "COINCHECK"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type

    def init_data(self) -> "CoincheckOrderBookData":
        if not self.has_been_json_encoded:
            self.order_book_data = (
                json.loads(self.order_book_info)
                if isinstance(self.order_book_info, str)
                else self.order_book_info
            )
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = self.order_book_data if isinstance(self.order_book_data, dict) else {}
        self.order_book_symbol_name = self.symbol_name
        self.bid_price_list = []
        self.ask_price_list = []
        self.bid_volume_list = []
        self.ask_volume_list = []
        for item in data.get("bids", []):
            if isinstance(item, list) and len(item) >= 2:
                self.bid_price_list.append(float(item[0]))
                self.bid_volume_list.append(float(item[1]))
        for item in data.get("asks", []):
            if isinstance(item, list) and len(item) >= 2:
                self.ask_price_list.append(float(item[0]))
                self.ask_volume_list.append(float(item[1]))

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name or "COINCHECK"

    def get_local_update_time(self) -> float | None:
        return self.local_update_time

    def get_symbol_name(self) -> str | None:
        return self.symbol_name

    def get_asset_type(self) -> str | None:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return None

    def get_bid_price_list(self) -> list[float] | None:
        self.init_data()
        return self.bid_price_list

    def get_ask_price_list(self) -> list[float] | None:
        self.init_data()
        return self.ask_price_list

    def get_bid_volume_list(self) -> list[float] | None:
        self.init_data()
        return self.bid_volume_list

    def get_ask_volume_list(self) -> list[float] | None:
        self.init_data()
        return self.ask_volume_list

    def get_bid_trade_nums(self) -> list[int] | None:
        return None

    def get_ask_trade_nums(self) -> list[int] | None:
        return None

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class CoincheckRequestOrderBookData(CoincheckOrderBookData):
    pass


class CoincheckWssOrderBookData(CoincheckOrderBookData):
    pass


__all__ = [
    "CoincheckOrderBookData",
    "CoincheckRequestOrderBookData",
    "CoincheckWssOrderBookData",
]
