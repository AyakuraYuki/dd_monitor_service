drop table if exists table_link;
create table table_link
(
    id    integer primary key autoincrement,
    title string,
    link  string not null
);