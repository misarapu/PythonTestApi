from .sector import Sector
from .query import Query
from database.db import Database


class Login:
    def __init__(self, name, session_id):
        print("Name: " + name)
        self.name = name
        self.session_id = session_id
        self.login = self.get_login()
        self.isNewUser = self.login is None

    def get_login(self):
        print("fetching user by name...")
        q = Query("SELECT * FROM artifydb.logins WHERE user_name=%s and session_id=%s", (self.name, self.session_id))
        return Database(q).get_one()

    # def get_user_sector(self):
    #     print("fetching user sector...")
    #     Database("SELECT * FROM artifydb.users_in_sectors JOIN artifydb.users ON user_id=id WHERE name=%s;",
    #              self.name).get_one()

    def add_user_in_sector(self, sector_id):
        print("adding...")
        print(self.name)
        print(self.session_id)
        print(sector_id)
        print("insert into login")
        q1 = Query("INSERT INTO artifydb.logins (user_name, session_id) VALUES (%s, %s);", (self.name, self.session_id))
        print("insert into user in sector")
        q2 = Query("INSERT INTO artifydb.users_in_sectors (login_id, sector_id) VALUES (LAST_INSERT_ID(), %s);", (sector_id,))
        queries = [q1, q2]
        print("after queries")
        Database(queries).add()

    def update_user_in_sector(self, sector_id):
        print("updating user sector...")
        q = Query("UPDATE artifydb.users_in_sectors SET sector_id=%s where login_id=%s;", (sector_id, self.login["id"]))
        queries = [q]
        Database(queries).add()

    def add_or_update_user_in_sector(self, sector_id):
        if self.isNewUser:
            self.add_user_in_sector(sector_id)
        else:
            self.update_user_in_sector(sector_id)
