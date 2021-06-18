import sqlite3 as database
import asyncio
import threading
import time
#import cryptography as crypt
import os
import datetime

#SB
#from pprint import pprint
#//from Google import Create_Service


class DatabaseConnection:
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

# Here freeing objects allocated of the DatabaseConnection and ServerClass
    def disconnectServer(self):
        return 0


class InterruptionManagementClass:
    def checkCalender(self):

        #SB
        #CLIENT_SECRET_FILE = 'client_secret.json'
        #API_NAME = 'calendar'
        #API_VERSION = 'v3'
        #SCOPES = ['https://www.googleapis.com/auth/calendar']
        #service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        #from apiclient.discovery import build
        #from google_auth_oauthlib.flow import InstalledAppFlow

        #scopes = ['https://www.googleapis.com/auth/calendar']
        #flow = InstalledAppFlow.from_client_secrets_file("C:/Users/Neel Shah/Desktop/Personal-Projects/YACApp/Backend/client_secret.json", scope=scopes)
        #flow.run_console

        return 0


class ServerClass:
    def sendMessages(self, sender, receiver, message):
        SendQuery = """ INSERT INTO Chat (Sender, Receiver, Message, DateTime) VALUES (?, ?, ?, ?); """
        Server = DatabaseConnection("C:/Users/Neel Shah/Desktop/Personal-Projects/YACApp/DB/YACApp.db")
        if Server.connectToDatabase():
            MessageWriter = Server.connection.cursor()
            message=(sender, receiver, message, datetime.datetime.now())
            MessageWriter.execute(SendQuery, message)
            Server.connection.commit()
            print("Message Sent to " + receiver + " Sucessfully")
            if Server.disconnectDatabase():
                del Server
                return 1
            else:
                del Server
                return 0

    def receiveMessages(self, receiver):
        RecieveQuery = """ select * from Chat where Receiver = ? """
        Server = DatabaseConnection("C:/Users/Neel Shah/Desktop/Personal-Projects/YACApp/DB/YACApp.db")
        if Server.connectToDatabase():
            MessageReader = Server.connection.cursor()
            MessageReader.execute(RecieveQuery, (receiver,))
            messages = MessageReader.fetchall()
            print("All Messages for " + receiver + " Loaded Sucessfully")
            for row in messages:
                print("Sender: ", row[0])
                print("Date Time Stamp: ", row[3])
                print("Message: ", row[2])
                print(" \n")
            if Server.disconnectDatabase():
                del Server
                return 1
            else:
                del Server
                return 0

    def __del__ (self):
        print("Object of class " + __class__.__name__ + " freed")

if __name__ == '__main__':
    server = ServerClass()
    print("ServerClass = " + str(server.receiveMessages("receiver")))
    #print("ServerClass = " + str(server.sendMessages("sender3", "receiver", """ sample message one
    #    new line """)))
