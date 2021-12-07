CREATE TABLE game(
    id bigint PRIMARY KEY,
    game_date TIMESTAMP,
    week SMALLINT,
    season SMALLINT,
    stadium_id INTEGER,
    broadcast VARCHAR(50),
    attendance SMALLINT,
    site VARCHAR(20)
)