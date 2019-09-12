CREATE TABLE IF NOT EXISTS table_link (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    title string,
    link  string,
    sort  INTEGER
);

CREATE TABLE IF NOT EXISTS table_channel (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    string,
    channel string UNIQUE NOT NULL
);
