# bt_api_coincheck

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_coincheck.svg)](https://pypi.org/project/bt_api_coincheck/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_coincheck.svg)](https://pypi.org/project/bt_api_coincheck/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_coincheck/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_coincheck/actions)
[![Docs](https://readthedocs.org/projects/bt-api-coincheck/badge/?version=latest)](https://bt-api-coincheck.readthedocs.io/)

---

<!-- English -->
# bt_api_coincheck

> **Coincheck exchange plugin for bt_api** — Unified REST API for **Spot** trading on Japan's Coincheck exchange.

`bt_api_coincheck` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **Coincheck** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-coincheck.readthedocs.io/ |
| Chinese Docs | https://bt-api-coincheck.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coincheck |
| PyPI | https://pypi.org/project/bt_api_coincheck/ |
| Issues | https://github.com/cloudQuant/bt_api_coincheck/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | Description |
|---|---|---|---|
| Spot | `COINCHECK___SPOT` | ✅ | Spot trading |

### Supported Operations

| Category | Operation | Spot |
|---|---|---|
| **Market Data** | `get_tick` / `get_ticker` | ✅ |
| | `get_depth` | ✅ |
| | `get_kline` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_server_time` | ✅ |
| | `get_deals` | ✅ |
| **Account** | `get_balance` | ✅ |
| | `get_account` | ✅ |
| **Trading** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `query_order` | ✅ |

### Supported Trading Pairs

- `BTC/JPY`, `ETH/JPY`, `SOL/JPY`, `XRP/JPY`, `ADA/JPY`, and 20+ more

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# Spot market data (public - no auth required)
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")

# Account balance (requires auth)
balance = api.get_balance("COINCHECK___SPOT")

# Place order (requires auth)
order = api.make_order(
    exchange_name="COINCHECK___SPOT",
    symbol="BTCJPY",
    volume=0.001,
    price=4500000,
    order_type="limit",
)
```

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_coincheck
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_coincheck
cd bt_api_coincheck
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_coincheck
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")
print(f"BTC/JPY price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINCHECK___SPOT",
    symbol="BTCJPY",
    volume=0.001,
    price=4500000,
    order_type="limit",
)
print(f"Order placed: {order}")
```

---

## Architecture

```
bt_api_coincheck/
├── plugin.py                     # register_plugin() — bt_api plugin entry point
├── registry_registration.py      # register_coincheck() — feeds / exchange_data registration
├── exchange_data/
│   └── __init__.py            # CoincheckExchangeDataSpot
├── feeds/
│   └── live_coincheck/
│       ├── request_base.py     # CoincheckRequestData — REST base class
│       └── spot.py            # CoincheckRequestDataSpot — spot operations
├── containers/
│   ├── accounts/              # Account containers
│   ├── balances/              # Balance containers
│   ├── bars/                  # Bar/Kline containers
│   ├── orderbooks/            # OrderBook containers
│   ├── orders/                # Order containers
│   └── tickers/               # Ticker containers
└── errors/
    └── __init__.py           # CoincheckErrorTranslator
```

---

## Error Handling

All Coincheck API errors are translated to bt_api_base `ApiError` subclasses:

| Condition | Error | Description |
|---|---|---|
| Balance insufficient | `INSUFFICIENT_BALANCE` | Insufficient account balance |
| Order not found | `ORDER_NOT_FOUND` | Order does not exist |
| Duplicate order | `DUPLICATE_ORDER` | Duplicate order detected |
| Rate limit | `RATE_LIMIT_EXCEEDED` | Too many requests |
| Auth failure | `INVALID_API_KEY` | Invalid API key or signature |

---

## Rate Limits

| Endpoint | Limit |
|---|---|
| Public endpoints | 200 requests/minute |
| Private endpoints | 200 requests/minute |

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-coincheck.readthedocs.io/ |
| **中文** | https://bt-api-coincheck.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coincheck/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 Coincheck 交易所插件** — 为日本 Coincheck 交易所的**现货**交易提供统一的 REST API。

`bt_api_coincheck` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **Coincheck** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-coincheck.readthedocs.io/ |
| 中文文档 | https://bt-api-coincheck.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coincheck |
| PyPI | https://pypi.org/project/bt_api_coincheck/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_coincheck/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | 说明 |
|---|---|---|---|
| 现货 | `COINCHECK___SPOT` | ✅ | 现货交易 |

### 支持的操作

| 类别 | 操作 | 现货 |
|---|---|---|
| **行情数据** | `get_tick` / `get_ticker` | ✅ |
| | `get_depth` | ✅ |
| | `get_kline` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_server_time` | ✅ |
| | `get_deals` | ✅ |
| **账户** | `get_balance` | ✅ |
| | `get_account` | ✅ |
| **交易** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `query_order` | ✅ |

### 支持的交易对

- `BTC/JPY`, `ETH/JPY`, `SOL/JPY`, `XRP/JPY`, `ADA/JPY` 等 20+ 交易对

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# 现货行情（公开接口，无需认证）
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")

# 账户余额（需要认证）
balance = api.get_balance("COINCHECK___SPOT")

# 下单（需要认证）
order = api.make_order(
    exchange_name="COINCHECK___SPOT",
    symbol="BTCJPY",
    volume=0.001,
    price=4500000,
    order_type="limit",
)
```

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_coincheck
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_coincheck
cd bt_api_coincheck
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_coincheck
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")
print(f"BTC/JPY 价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINCHECK___SPOT",
    symbol="BTCJPY",
    volume=0.001,
    price=4500000,
    order_type="limit",
)
print(f"订单已下单: {order}")
```

---

## 架构

```
bt_api_coincheck/
├── plugin.py                     # register_plugin() — bt_api 插件入口点
├── registry_registration.py      # register_coincheck() — feeds / exchange_data 注册
├── exchange_data/
│   └── __init__.py            # CoincheckExchangeDataSpot
├── feeds/
│   └── live_coincheck/
│       ├── request_base.py     # CoincheckRequestData — REST 基类
│       └── spot.py            # CoincheckRequestDataSpot — 现货操作
├── containers/
│   ├── accounts/              # 账户容器
│   ├── balances/              # 余额容器
│   ├── bars/                  # K线容器
│   ├── orderbooks/            # 订单簿容器
│   ├── orders/                # 订单容器
│   └── tickers/               # 行情容器
└── errors/
    └── __init__.py           # CoincheckErrorTranslator
```

---

## 错误处理

所有 Coincheck API 错误均翻译为 bt_api_base `ApiError` 子类：

| 条件 | 错误 | 说明 |
|---|---|---|
| 余额不足 | `INSUFFICIENT_BALANCE` | 账户余额不足 |
| 订单未找到 | `ORDER_NOT_FOUND` | 订单不存在 |
| 重复订单 | `DUPLICATE_ORDER` | 检测到重复订单 |
| 限流 | `RATE_LIMIT_EXCEEDED` | 请求过于频繁 |
| 认证失败 | `INVALID_API_KEY` | API key 或签名无效 |

---

## 限流配置

| 端点 | 限制 |
|---|---|
| 公开接口 | 200 次/分钟 |
| 私有接口 | 200 次/分钟 |

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-coincheck.readthedocs.io/ |
| **中文文档** | https://bt-api-coincheck.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coincheck/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com