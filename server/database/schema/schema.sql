DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO user (username, email) VALUES ('john_doe', 'john@example.com');
INSERT INTO user (username, email) VALUES ('jane_doe', 'jane@example.com');