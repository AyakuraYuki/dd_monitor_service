DROP TABLE IF EXISTS table_link;
CREATE TABLE table_link (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    title string,
    link  string,
    sort  INTEGER
);

DROP TABLE IF EXISTS table_channel;
CREATE TABLE table_channel (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    string,
    channel string UNIQUE NOT NULL
);
