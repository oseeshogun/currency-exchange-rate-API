from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

from external_apis import Provider, get_exchange_rates

_CACHE_TTL = timedelta(hours=24)
_rate_cache: Dict[Tuple[str, Tuple[str, ...], Optional[Provider]], Tuple[datetime, dict]] = {}


def get_cached_rates(
    target: str, currencies_list: List[str], provider: Optional[Provider]
) -> dict:
    cache_key = (target.lower(), tuple(currencies_list), provider)
    cached = _rate_cache.get(cache_key)
    if cached:
        cached_at, cached_data = cached
        if datetime.now() - cached_at < _CACHE_TTL:
            return cached_data

    data = get_exchange_rates(target, currencies_list, provider)
    _rate_cache[cache_key] = (datetime.now(), data)
    return data
