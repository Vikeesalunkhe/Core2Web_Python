import sqlite3

conn = sqlite3.connect("project.db")
cursorObj = conn.cursor()

query = "update Players set PlayerName = 'virat kohli' where gender = 'M'"

cursorObj.execute(query)
conn.commit()

query2 = "select * from Players"
cursorObj.execute(query2)

data = cursorObj.fetchall()

for i in data:
    print(i)

conn.close()

