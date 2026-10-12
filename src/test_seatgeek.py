
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("SEATGEEK_CLIENT_ID")

if not API_KEY:
    raise ValueError("SeatGeek client ID not found.")

# SeatGeek API endpoint
URL = "https://api.seatgeek.com/2/events"

params = {
    "client_id": API_KEY,
    "performers.slug": "dallas-cowboys",
    "datetime_utc.gte": "2026-10-11",
    "per_page": 10
}

print("Connecting to SeatGeek...")

response = requests.get(URL, params=params, timeout=20)

print("HTTP Status:", response.status_code)

response.raise_for_status()

data = response.json()
events = data.get("events", [])

print(f"Found {len(events)} events")

for event in events:
    stats = event.get("stats") or {}

    print("\nEvent:", event.get("title"))
    print("Date:", event.get("datetime_local"))
    print("Event ID:", event.get("id"))
    print("Lowest price:", stats.get("lowest_price"))
    print("Average price:", stats.get("average_price"))
    print("Stats:", event.get("stats"))
