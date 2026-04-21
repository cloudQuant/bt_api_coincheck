from __future__ import annotations

from bt_api_base.gateway.registrar import GatewayRuntimeRegistrar
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_coincheck import __version__
from bt_api_coincheck.registry_registration import register_coincheck


def get_plugin_info() -> PluginInfo:
    return PluginInfo(
        name="bt_api_coincheck",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("COINCHECK___SPOT",),
        supported_asset_types=("SPOT",),
        plugin_module="bt_api_coincheck.plugin",
    )


def register_plugin(
    registry: ExchangeRegistry | type[ExchangeRegistry],
    runtime_factory: type[GatewayRuntimeRegistrar],
) -> PluginInfo:
    del runtime_factory
    register_coincheck(registry)
    return get_plugin_info()
