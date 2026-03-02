from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI

from external_apis import Provider, get_exchange_rates

app = FastAPI()


@app.get("/health")
def health():
    return dict(time=datetime.now())


@app.get("/rate")
def exchange_rate(target: str, currencies: str, provider: Optional[Provider] = None):
    currencies_list: List[str] = [c.lower() for c in currencies.split(",") if c.strip()]
    return get_exchange_rates(target, currencies_list, provider)
