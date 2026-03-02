"""
API from https://currencyapi.net/
"""

from typing import Dict, List

import httpx

from config import get_settings


def get_exchange_rates_currencyapi_net(
    target: str,
    currencies: List[str],
) -> Dict[str, float]:
    settings = get_settings()
    url = f"https://currencyapi.net/api/v2/rates?key={settings.currency_api_net_api_key}&base={target}&output=JSON"
    response = httpx.get(url)
    data = response.json()
    rates = data["rates"]
    return {
        currency: rates[currency.upper()]
        for currency in currencies
        if currency.upper() in rates.keys()
    }
