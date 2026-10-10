
-- 1. Verify the total number of games
SELECT COUNT(*) AS total_games
FROM games;

-- 2. Check for duplicate game IDs
SELECT game_id, COUNT(*) AS occurrences
FROM games
GROUP BY game_id
HAVING COUNT(*) > 1;

-- 3. Count the number of unique MLB teams
SELECT COUNT(DISTINCT team_id) AS total_teams
FROM (
    SELECT home_team_id AS team_id FROM games
    UNION
    SELECT away_team_id FROM games
);

-- 4. Find all Red Sox home games
SELECT  game_date,
        home_team,
        away_team
FROM games
WHERE home_team = 'Boston Red Sox'
ORDER BY game_date;

-- 5. Count Red Sox home games
SELECT COUNT(*) AS red_sox_home_games
FROM games
WHERE home_team_id = 111;
