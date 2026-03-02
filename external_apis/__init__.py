from typing import Dict, List

from .currency_api_com import get_exchange_rates_currencyapi_com
from .currency_api_net import get_exchange_rates_currencyapi_net
from .fawazahmed_exchange_api import fw_exchange_rates


def get_exchange_rates(
    base_currency: str,
    currencies: List[str],
) -> Dict[str, float]:
    try:
        return get_exchange_rates_currencyapi_net(base_currency, currencies)
    except Exception as e:
        print(e)
        try:
            return get_exchange_rates_currencyapi_com(base_currency, currencies)
        except Exception as e:
            print(e)
            return fw_exchange_rates(base_currency, currencies)
