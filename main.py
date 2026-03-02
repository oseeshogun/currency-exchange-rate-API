from datetime import datetime
from typing import List, Optional

from fastapi import Depends, FastAPI, Security
from fastapi.exceptions import HTTPException
from fastapi.security import APIKeyHeader

from config import Settings, get_settings
from external_apis import Provider
from utils import get_cached_rates

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def validate_api_key(
    api_key: str = Security(api_key_header), settings: Settings = Depends(get_settings)
):
    if api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key


@app.get("/healthz")
def health():
    return dict(time=datetime.now())


@app.get("/rate", dependencies=[Depends(validate_api_key)])
def exchange_rate(target: str, currencies: str, provider: Optional[Provider] = None):
    currencies_list: List[str] = [c.lower() for c in currencies.split(",") if c.strip()]
    return get_cached_rates(target, currencies_list, provider)
