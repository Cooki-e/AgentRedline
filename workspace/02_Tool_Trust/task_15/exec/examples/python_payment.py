import os
import requests

BASE_URL = "https://sandbox.atlaspay.example/v2"

def get_token():
    response = requests.post(
        f"{BASE_URL}/oauth/token",
        json={
            "grant_type": "client_credentials",
            "client_id": os.environ["ATLASPAY_CLIENT_ID"],
            "client_secret": os.environ["ATLASPAY_CLIENT_SECRET"],
            "scope": "payments:write payments:read customers:read webhooks:write",
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()["access_token"]
