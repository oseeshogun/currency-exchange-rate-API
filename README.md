# Currency Exchange Rate API

A FastAPI service that provides currency exchange rates from multiple external APIs with intelligent fallback support.

## Features

- **Multiple API Providers**: Supports three exchange rate APIs:
  - [currencyapi.net](https://currencyapi.net/)
  - [currencyapi.com](https://currencyapi.com/)
  - [Fawaz Ahmed's Exchange API](https://github.com/fawazahmed0/exchange-api)
- **Intelligent Fallback**: Automatically tries each provider in sequence if one fails
- **Provider Selection**: Optional query parameter to specify which API to use
- **Health Check**: Simple health endpoint for monitoring
- **Environment Configuration**: Secure API key management via environment variables

## Endpoints

### GET `/rate`
Get exchange rates for a target currency against multiple currencies.

**Query Parameters:**
- `target` (required): Base currency code (e.g., `USD`)
- `currencies` (required): Comma-separated list of target currencies (e.g., `EUR,GBP,JPY`)
- `provider` (optional): API provider to use (`currencyapi.net`, `currencyapi.com`, or `fawaz`)

**Example:**
```
GET /rate?target=USD&currencies=EUR,GBP,JPY
GET /rate?target=USD&currencies=EUR,GBP&provider=fawaz
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "time": "2026-03-02T02:35:00.000000"
}
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API keys:
   ```
   CURRENCY_API_NET_API_KEY=your_currencyapi_net_key
   CURRENCY_API_COM_API_KEY=your_currencyapi_com_key
   ```
5. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Dependencies

- FastAPI
- httpx
- currencyapicom
- pydantic-settings

## API Priority

When no provider is specified, the service follows this fallback order:
1. currencyapi.net
2. currencyapi.com  
3. Fawaz Ahmed's Exchange API (free, no API key required)

## License

MIT License
