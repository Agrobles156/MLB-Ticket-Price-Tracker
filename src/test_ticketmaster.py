from dotenv import load_dotenv
from pathlib import Path
import requests
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("TICKETMASTER_API_KEY")
#print(API_KEY)

if not API_KEY:
    raise ValueError("Ticketmaster API key not found.")

URL = "https://app.ticketmaster.com/discovery/v2/events.json"

params = {
    "apikey": API_KEY,
    "classificationName": "baseball",
    "countryCode": "US",
    "size": 200
}

print("Connecting to Ticketmaster...")

response = requests.get(URL, params=params, timeout=20)

print("HTTP Staus:", response.status_code)

response.raise_for_status()

data = response.json()
events = data.get("_embedded", {}).get("events", [])

print(f"Found {len(events)} events")

events_with_prices = 0

for event in events:
    price_ranges = event.get("priceRanges")

    if price_ranges:
        events_with_prices += 1
        print("\nEvent:", event.get("name"))
        print("Date:", event.get("dates", {}).get("start", {}).get("localDate"))
        print("Prices:", price_ranges)

print(f"\nEvents checked: {len(events)}")
print(f"Events with prices: {events_with_prices}")