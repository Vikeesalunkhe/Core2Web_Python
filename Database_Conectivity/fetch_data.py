import sqlite3

conn = sqlite3.connect("project.db")
cursorObj = conn.cursor()

query = "select * from Players"

cursorObj.execute(query)

data = cursorObj.fetchall()
print(data)

for i in data:
    print(i)

conn.close()
