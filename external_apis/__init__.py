from enum import Enum
from typing import Dict, List, Optional

from .currency_api_com import get_exchange_rates_currencyapi_com
from .currency_api_net import get_exchange_rates_currencyapi_net
from .fawazahmed_exchange_api import fw_exchange_rates


class Provider(str, Enum):
    CURRENCY_API_NET = "currencyapi.net"
    CURRENCY_API_COM = "currencyapi.com"
    FAWAZ = "fawaz"


def get_exchange_rates(
    base_currency: str,
    currencies: List[str],
    provider: Optional[Provider] = None,
) -> Dict[str, float]:
    if provider == Provider.CURRENCY_API_NET:
        return get_exchange_rates_currencyapi_net(base_currency, currencies)
    if provider == Provider.CURRENCY_API_COM:
        return get_exchange_rates_currencyapi_com(base_currency, currencies)
    if provider == Provider.FAWAZ:
        return fw_exchange_rates(base_currency, currencies)

    try:
        return get_exchange_rates_currencyapi_net(base_currency, currencies)
    except Exception as e:
        print(e)
    try:
        return get_exchange_rates_currencyapi_com(base_currency, currencies)
    except Exception as e:
        print(e)
    return fw_exchange_rates(base_currency, currencies)
