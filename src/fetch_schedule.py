
import json
from pathlib import Path

import requests

print("Starting MLB schedule fetch...")

# MLB's public Stats API
API_URL = "https://statsapi.mlb.com/api/v1/schedule"

# Parameters for the 2027 regular season
params = {
    "sportId": 1,
    "season": 2027,
    "gameType": "R"
}

# Request schedule data from MLB
response = requests.get(API_URL, params=params, timeout=30)
response.raise_for_status()

data = response.json()

# Save the raw API response
project_root = Path(__file__).resolve().parent.parent
output_path = project_root / "Data" / "raw" / "mlb_schedule_2027.json"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

# Count games returned
games = [
    game
    for date in data.get("dates", [])
    for game in date.get("games", [])
]

print(f"Successfully retrieved {len(games)} MLB games.")
print(f"Data saved to: {output_path}")

if not games:
    print("No games returned. Check schedule availability and API parameters.")
else:
    first_game = games[0]
    print("Example game:", first_game["teams"])
