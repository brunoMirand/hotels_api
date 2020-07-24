import sqlite3


class ConnectionDatabase:
    def connection_database(self):
        connection = sqlite3.connect('storage.db')
        return connection.cursor()
