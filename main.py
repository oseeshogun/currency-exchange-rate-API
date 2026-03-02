from datetime import datetime
from typing import List

from fastapi import FastAPI

from external_apis import get_exchange_rates

app = FastAPI()


@app.get("/health")
def health():
    return dict(time=datetime.now())


@app.get("/rate")
def exchange_rate(target: str, currencies: str):
    currencies_list: List[str] = []
    if currencies.split(","):
        currencies_list = currencies.lower().split(",")

    return get_exchange_rates(target, currencies_list)
