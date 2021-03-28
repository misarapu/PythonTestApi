from .sector import Sector
from .query import Query
from database.db import Database


class Login:
    def __init__(self, name, session_id):
        self.name = name
        self.session_id = session_id
        self.login = self.get_login()
        self.isNewUser = self.login is None

    def get_login(self):
        print("fetching user by name...")
        q = Query("SELECT * FROM artifydb.logins WHERE user_name=%s and session_id=%s",
                  (self.name, self.session_id))
        return Database(q).get_one()

    def add_user_in_sector(self, sector_id):
        print("adding...")
        print("insert into login")
        q1 = Query("INSERT INTO artifydb.logins (user_name, session_id) VALUES (%s, %s);",
                   (self.name, self.session_id))
        q2 = Query(
            "INSERT INTO artifydb.users_in_sectors (login_id, sector_id) VALUES (LAST_INSERT_ID(), %s);", (sector_id,))
        queries = [q1, q2]
        Database(queries).add()

    def update_user_in_sector(self, sector_id):
        print("updating user sector...")
        q = Query("UPDATE artifydb.users_in_sectors SET sector_id=%s where login_id=%s;",
                  (sector_id, self.login["id"]))
        queries = [q]
        Database(queries).add()

    def add_or_update_user_in_sector(self, sector_id):
        if self.isNewUser:
            self.add_user_in_sector(sector_id)
        else:
            self.update_user_in_sector(sector_id)
