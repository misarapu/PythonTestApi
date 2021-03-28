from database.db import Database
from .query import Query


class Sector:
    def __init__(self, group_1, group_2, group_3, group_4):
        self.group_1 = group_1
        self.group_2 = group_2
        self.group_3 = group_3
        self.group_4 = group_4

    def get_sectors():
        q = Query(
            "SELECT * FROM artifydb.sectors GROUP BY group_1, group_2, group_3, group_4", None)
        return Database(q).get_all()
