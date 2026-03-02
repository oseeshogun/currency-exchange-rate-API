from typing import Dict, List

import currencyapicom

from config import Settings


def get_exchange_rates_currencyapi_com(
    base_currency: str, currencies: List[str]
) -> Dict[str, float]:
    settings = Settings()
    client = currencyapicom.Client(settings.currency_api_com_api_key)
    response = client.latest(
        base_currency=base_currency.upper(),
        currencies=[currency.upper() for currency in currencies],
    )
    data = response.get("data", {})
    exchange_rates = {
        currency.upper(): rate["value"] for currency, rate in data.items()
    }
    return exchange_rates
