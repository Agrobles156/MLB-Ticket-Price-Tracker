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