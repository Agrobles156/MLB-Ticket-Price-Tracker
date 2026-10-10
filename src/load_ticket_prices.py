import sqlite3
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_ROOT / "Data" / "mlb_tickets.db"

def save_ticket_price(game_id, source, lowest_price):
    collected_at = datetime.now(timezone.utc).isoformat()

    with sqlite3.connect(DATABASE_FILE) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        conn.execute(
            """
            INSERT INTO ticket_prices (
                game_id,
                collected_at,
                source,
                lowest_price
            )
            VALUES (?, ?, ?, ?)
            """,
            (game_id, collected_at, source, lowest_price)
        )

        conn.commit()

        print(f"Saved ticket price: ${lowest_price:.2f}")

if __name__ == "__main__":
    print("Ticket price loader ready.")