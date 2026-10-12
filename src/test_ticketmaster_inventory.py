
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("TICKETMASTER_API_KEY")

if not API_KEY:
    raise ValueError("Ticketmaster API key not found.")

URL = "https://app.ticketmaster.com/inventory-status/v1/availability"

params = {
    "apikey": API_KEY,
    "events": "G5vVZ_oiA65dw"
}

print("Checking Ticketmaster inventory...")

response = requests.get(URL, params=params, timeout=20)

print("HTTP Status:", response.status_code)

if response.status_code != 200:
    print("Response:", response.text[:1000])

response.raise_for_status()

data = response.json()

print("Inventory response:")
print(data)
