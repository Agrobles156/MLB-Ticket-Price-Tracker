
import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = PROJECT_ROOT / "Data" / "processed" / "mlb_schedule_2027.csv"
DATABASE_FILE = PROJECT_ROOT / "Data" / "mlb_tickets.db"
SCHEMA_FILE = PROJECT_ROOT / "SQL" / "schema.sql"


def load_schedule():
    # Read transformed schedule data
    df = pd.read_csv(CSV_FILE)

    # Connect to SQLite database
    with sqlite3.connect(DATABASE_FILE) as conn:

        # Create tables if they don't exist
        with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
            conn.executescript(file.read())

        # Insert new games or update existing games
        query = """
        INSERT INTO games (
            game_id,
            game_date,
            home_team_id,
            home_team,
            away_team_id,
            away_team,
            game_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)

        ON CONFLICT(game_id) DO UPDATE SET
            game_date = excluded.game_date,
            home_team_id = excluded.home_team_id,
            home_team = excluded.home_team,
            away_team_id = excluded.away_team_id,
            away_team = excluded.away_team,
            game_status = excluded.game_status;
        """

        records = list(df.itertuples(index=False, name=None))

        conn.executemany(query, records)
        conn.commit()

        print(f"Successfully processed {len(records)} games.")


if __name__ == "__main__":
    load_schedule()
