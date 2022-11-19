from Scraper.Parser.JSONParser import JSON
from Server.ConnectionAdmin import ConnectionAdmin


def auth(user: JSON) -> JSON:
    return user


def readAllUsers() -> JSON:
    connection = ConnectionAdmin()
    register = connection.GetCollection("admin").system.users.find_one({})
    register["userId"] = register['userId'].as_uuid().urn
    return register


def create():
    pass


def delete():
    pass


def update():
    pass


def read():
    pass
