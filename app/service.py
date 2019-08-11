from app.database import get_database
from app.model import Link


def links(query=''):
    result = []
    sql = "select * from table_link where title like '%' || ? || '%'"
    parameters = (query,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        for row in cursor:
            link = Link(_id=row['id'], title=row['title'], link=row['link'])
            result.append(link)

    return result


def get_link(_id=0):
    if _id == 0:
        return None
    sql = "select * from table_link where id = ?"
    parameters = (_id,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        if len(cursor) == 1:
            row = cursor[0]
            link = Link(_id=row['id'], title=row['title'], link=row['link'])
        else:
            link = None

    return link


def __update(sql='', parameters=None):
    if sql == '' or ('?' in sql and parameters is None):
        return 0
    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        row_count = cursor.rowcount
        db.commit()
    return row_count


def insert(link: Link = None):
    if link is None:
        return 0
    sql = "insert into table_link (title, link) VALUES (?, ?)"
    parameters = (link.title, link.link,)
    return __update(sql, parameters)


def delete(_id=0):
    if _id == 0:
        return 0
    sql = "delete from table_link where id = ?"
    parameters = (_id,)
    return __update(sql, parameters)
