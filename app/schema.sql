DROP TABLE IF EXISTS table_link;
CREATE TABLE table_link (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    title string,
    link  string,
    sort  INTEGER
);