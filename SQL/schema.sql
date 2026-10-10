CREATE TABLE IF NOT EXISTS games(
    game_id INTEGER PRIMARY KEY,
    game_date TEXT NOT NULL,
    home_team_id INTEGER NOT NULL,
    home_team TEXT NOT NULL,
    away_team_id INTEGER NOT NULL,
    away_team TEXT NOT NULL,
    game_status TEXT NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_games_game_id
ON games(game_id);

CREATE TABLE IF NOT EXISTS ticket_prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    collected_at TEXT NOT NULL,
    source TEXT NOT NULL,
    lowest_price REAL NOT NULL CHECK (lowest_price >= 0),
    currency TEXT NOT NULL DEFAULT 'USD',

    FOREIGN KEY (game_id) REFERENCES games(game_id),

    UNIQUE (game_id, collected_at, source)
);