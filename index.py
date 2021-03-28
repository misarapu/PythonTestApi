from tornado.ioloop import IOLoop
from tornado.web import (Application, RequestHandler)

from database import db
import json
from models.sector import Sector
from models.login import Login


class SectorsHandler(RequestHandler):
    def get(self):
        try:
            self.set_header("Content-Type", 'application/json')
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Methods", "*")
            self.write(json.dumps(Sector.get_sectors()))
            self.set_status(200)
        except Exception as e:
            print(e)
            self.set_status(400)


class LoginHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Content-type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    def post(self):
        try:
            self.json_args = json.loads(self.request.body)
            user = self.json_args['user_name']
            sector = self.json_args['sector_id']
            # couldn't implement the session logic
            Login(user, "first_session").add_or_update_user_in_sector(sector)
            self.set_status(200)
        except Exception as e:
            print(e)
            self.set_status(400)

    def options(self):
        pass


class InitialiseApp(Application):
    def __init__(self):
        handlers = [
            (r"/api/sectors", SectorsHandler),
            (r"/api/logins", LoginHandler)
        ]

        server_settings = {
            "debug": True,
            "autoreload": True
        }

        Application.__init__(self, handlers, **server_settings)


def run_server():
    app = InitialiseApp()
    app.listen(3000)
    #IOLoop.current().stop()
    IOLoop.current().start()


if __name__ == '__main__':
    run_server()
