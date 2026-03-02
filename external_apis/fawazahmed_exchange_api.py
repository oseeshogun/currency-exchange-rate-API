"""
API for Fawaz Ahmed's Exchange Rates API
Repo: https://github.com/fawazahmed0/exchange-api
"""

from datetime import datetime, timedelta
from typing import Dict, List

import httpx


def fw_exchange_rates(base_currency: str, currencies: List[str]) -> Dict[str, float]:
    url: str = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base_currency.lower()}.json"
    response = httpx.get(url)
    data = response.json()
    str_date = data["date"]
    date_format = "%Y-%m-%d"
    latest_update = datetime.strptime(str_date, date_format)
    last_month_date = datetime.now() - timedelta(days=30)

    if latest_update < last_month_date:
        raise ValueError("Exchange rates are not available for the last month.")

    rates = data[base_currency]

    return {currency: rates[currency] for currency in currencies}
