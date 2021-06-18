import sqlite3 as database
import asyncio
import threading
import time
#import cryptography as crypt
import os



class DatabseConnection:
    connection = None
# add fully qualified file path as string between double quotes
    def __init__(self, filepath):
        self.filepath = filepath

    def connectToDatabase(self):
        try:
            self.connection = database.connect(self.filepath)
            print(self.connection)
            print("Connection Sucessfull to the database " + self.filepath)
        except database.Error as e:
            print(e)
        finally:
            if self.connection:
                return 1
            else:
                return 0
    def disconnectDatabase(self):
        try:
            self.connection.close()
            print("Database Connection Disconnected")
            self.connection = None
        except database.Error as e:
            print(e)
        finally:
            if self.connection is None:
                return 1
            else:
                return 0

    def __del__(self):
        print("Object of class " + __class__.__name__ + " freed")


class ServerConnectionClass:
    def connectToClient(self):
        return 0

    def checkConnection(self):
        return 0

    def reconnectToClient(self):
        return 0


class InterruptionManagementClass:
    def checkCalender(self):
        return 0


class ServerClass:
    def sendMessages(self):
        db = DatabseConnection("C:/Users/Neel Shah/Desktop/Personal-Projects/YACApp/DB/YACApp.db")
        if db.connectToDatabase():
            print("inside send logic")
            if db.disconnectDatabase():
                del db
                return 1
            else:
                del db
                return 0

    def receiveMessages(self):
        return 0

if __name__ == '__main__':
    server = ServerClass()
    print("sendMessages " + str(server.sendMessages()))
