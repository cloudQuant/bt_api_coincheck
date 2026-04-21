from __future__ import annotations

from unittest.mock import MagicMock

from bt_api_coincheck.feeds.live_coincheck.request_base import CoincheckRequestData


def test_coincheck_disconnect_closes_http_client() -> None:
    request_data = CoincheckRequestData()
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()
