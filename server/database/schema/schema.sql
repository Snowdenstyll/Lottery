DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO user (username, email) VALUES ('john_doe', 'john@example.com');
INSERT INTO user (username, email) VALUES ('jane_doe', 'jane@example.com');

DROP TABLE IF EXISTS lottery_numbers;

CREATE TABLE lottery_numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT NOT NULL,
    draw_date DATE NOT NULL,
    draw_time CHAR(1) CHECK (draw_time IN ('A', 'P')) NOT NULL,
    numbers TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (game_name, draw_date, draw_time)
);