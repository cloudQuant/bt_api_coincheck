"""Tests for CoincheckExchangeData container."""

from __future__ import annotations

from bt_api_coincheck.exchange_data import CoincheckExchangeData


class TestCoincheckExchangeData:
    """Tests for CoincheckExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = CoincheckExchangeData()

        assert exchange.exchange_name == "coincheck"
