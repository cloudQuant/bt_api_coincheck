# Coincheck Exchange Plugin Documentation

## English

### Overview

`bt_api_coincheck` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **Coincheck** exchange. Coincheck is a Japanese cryptocurrency exchange offering spot trading.

### Installation

```bash
pip install bt_api_coincheck
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

### Quick Start

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# Get ticker (public)
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")

# Get balance (requires auth)
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

### Supported Operations

| Category | Operation | Status |
|---|---|---|
| Market Data | `get_tick` | ✅ |
| | `get_depth` | ✅ |
| | `get_kline` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_server_time` | ✅ |
| | `get_deals` | ✅ |
| Account | `get_balance` | ✅ |
| | `get_account` | ✅ |
| Trading | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `query_order` | ✅ |

### Supported Trading Pairs

- `BTC/JPY`, `ETH/JPY`, `SOL/JPY`, `XRP/JPY`, `ADA/JPY`, and 20+ more

### Architecture

```
bt_api_coincheck/
├── plugin.py                     # Plugin entry point
├── registry_registration.py      # Feed and exchange data registration
├── exchange_data/               # Exchange data classes
├── feeds/                      # REST API feeds
│   └── live_coincheck/
│       ├── request_base.py     # Base REST class
│       └── spot.py            # Spot operations
├── containers/                  # Data containers
│   ├── accounts/
│   ├── balances/
│   ├── bars/
│   ├── orderbooks/
│   ├── orders/
│   └── tickers/
└── errors/                     # Error translation
```

### Error Handling

| Condition | Error | Description |
|---|---|---|
| Balance insufficient | `INSUFFICIENT_BALANCE` | Insufficient account balance |
| Order not found | `ORDER_NOT_FOUND` | Order does not exist |
| Duplicate order | `DUPLICATE_ORDER` | Duplicate order detected |
| Rate limit | `RATE_LIMIT_EXCEEDED` | Too many requests |
| Auth failure | `INVALID_API_KEY` | Invalid API key or signature |

### Rate Limits

| Endpoint | Limit |
|---|---|
| Public endpoints | 200 requests/minute |
| Private endpoints | 200 requests/minute |

---

## 中文

### 概述

`bt_api_coincheck` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **Coincheck** 交易所。Coincheck 是日本加密货币交易所，提供现货交易服务。

### 安装

```bash
pip install bt_api_coincheck
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

### 快速开始

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINCHECK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# 获取行情（公开接口）
ticker = api.get_tick("COINCHECK___SPOT", "BTCJPY")

# 获取余额（需要认证）
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

### 支持的操作

| 类别 | 操作 | 状态 |
|---|---|---|
| 行情数据 | `get_tick` | ✅ |
| | `get_depth` | ✅ |
| | `get_kline` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_server_time` | ✅ |
| | `get_deals` | ✅ |
| 账户 | `get_balance` | ✅ |
| | `get_account` | ✅ |
| 交易 | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `query_order` | ✅ |

### 支持的交易对

- `BTC/JPY`, `ETH/JPY`, `SOL/JPY`, `XRP/JPY`, `ADA/JPY` 等 20+ 交易对

### 架构

```
bt_api_coincheck/
├── plugin.py                     # 插件入口点
├── registry_registration.py      # Feed 和 exchange data 注册
├── exchange_data/               # 交易所数据类
├── feeds/                      # REST API feeds
│   └── live_coincheck/
│       ├── request_base.py     # REST 基类
│       └── spot.py            # 现货操作
├── containers/                  # 数据容器
│   ├── accounts/
│   ├── balances/
│   ├── bars/
│   ├── orderbooks/
│   ├── orders/
│   └── tickers/
└── errors/                     # 错误翻译
```

### 错误处理

| 条件 | 错误 | 说明 |
|---|---|---|
| 余额不足 | `INSUFFICIENT_BALANCE` | 账户余额不足 |
| 订单未找到 | `ORDER_NOT_FOUND` | 订单不存在 |
| 重复订单 | `DUPLICATE_ORDER` | 检测到重复订单 |
| 限流 | `RATE_LIMIT_EXCEEDED` | 请求过于频繁 |
| 认证失败 | `INVALID_API_KEY` | API key 或签名无效 |

### 限流配置

| 端点 | 限制 |
|---|---|
| 公开接口 | 200 次/分钟 |
| 私有接口 | 200 次/分钟 |

---

## Resources

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-coincheck.readthedocs.io/ |
| Chinese Docs | https://bt-api-coincheck.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coincheck |
| PyPI | https://pypi.org/project/bt_api_coincheck/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |