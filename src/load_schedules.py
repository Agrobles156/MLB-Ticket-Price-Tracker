
import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = PROJECT_ROOT / "Data" / "processed" / "mlb_schedule_2027.csv"
DATABASE_FILE = PROJECT_ROOT / "Data" / "mlb_tickets.db"
SCHEMA_FILE = PROJECT_ROOT / "SQL" / "schema.sql"

# Read the processed dataset
df = pd.read_csv(CSV_FILE)

# Connect to SQLite
conn = sqlite3.connect(DATABASE_FILE)

try:
    # Create tables from SQL schema
    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        conn.executescript(file.read())

    # Load game records into the database
    df.to_sql(
        "games",
        conn,
        if_exists="append",
        index=False
    )

    conn.commit()

    print(f"Successfully loaded {len(df)} games into SQLite.")

finally:
    conn.close()
