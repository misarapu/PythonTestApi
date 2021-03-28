import mysql.connector
from models.query import Query


class Database:
    def __init__(self, queries):
        self.queries = queries
        self.fetch_all = False
        self.fetch_one = False
        self.insert = False

    def execute(self):

        def inner_execute(q):
          if q.params is None:
            cursor.execute(q.query)
          else:
            cursor.execute(q.query, q.params)

        def execute(self):
            if isinstance(self.queries, list):
                for q in self.queries:
                  inner_execute(q)
            else:
                inner_execute(self.queries)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="sJ5L8&6LK0vHM{}8",
                database="artifydb",
            )

            conn.autocommit = False
            cursor = conn.cursor(dictionary=True)
            execute(self)
            if self.fetch_one:
                return cursor.fetchone()
            if self.fetch_all:
                return cursor.fetchall()
            if self.insert:
                conn.commit()

        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("connection is closed")

    def add(self):
        self.insert = True
        self.execute()

    def get_all(self):
        self.fetch_all = True
        return self.execute()

    def get_one(self):
        self.fetch_one = True
        return self.execute()
