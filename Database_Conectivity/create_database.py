
import sqlite3

conn = sqlite3.connect("project.db")
cursorObj = conn.cursor()

query = '''create table Players (
                jersyNo INTEGER,
                PlayerName varchar(20),
                TeamName varchar(20),
                gender varchar(20)
            )'''


cursorObj.execute(query)


conn.close()
