import json
from pathlib import Path
import pandas as pd

# Project Directory
PROJECT_ROOT =  Path(__file__).resolve().parent.parent

# Input and Output Paths
INPUT_FILE = PROJECT_ROOT / "Data" / "raw" / "mlb_schedule_2027.json"
OUTPUT_FILE = PROJECT_ROOT / "Data" / "processed" / "mlb_schedule_2027.csv"

# Read the raw JSON
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

# Store transformed game records
games = []

for date_entry in data["dates"]:
    for game in date_entry["games"]:

        game_record = {
            "game_id": game["gamePk"],
            "game_date": game["officialDate"],
            "home_team_id": game["teams"]["home"]["team"]["id"],
            "home_team": game["teams"]["home"]["team"]["name"],
            "away_team_id": game["teams"]["away"]["team"]["id"],
            "away_team": game["teams"]["away"]["team"]["name"],
            "game_status": game["status"]["detailedState"]
        }

        games.append(game_record)

# Convert to DataFrame
df = pd.DataFrame(games)

# Basic validation
if df["game_id"].duplicated().any():
    raise ValueError("Duplicate game IDs detected!")

if df["game_id"].isna().any():
    raise ValueError("Missing game IDs detected!")

# Convert date column
df["game_date"] = pd.to_datetime(df["game_date"])

# Sort games chronologically
df = df.sort_values("game_date")

# Create output directory
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Export cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print(f"Successfully transformed {len(df)} games.")
print(f"CSV saved to: {OUTPUT_FILE}")
print(df.head())