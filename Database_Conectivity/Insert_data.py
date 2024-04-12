import sqlite3

conn = sqlite3.connect("project.db")
cursorObj = conn.cursor()

query1 = "insert into Players values (18, 'virat', 'M', 'IND')"
query2 = "insert into Players values (7, 'dhoni', 'M', 'IND')"
query3 = "insert into players values (34, 'mandana', 'F', 'AUS')"

cursorObj.execute(query1)
cursorObj.execute(query2)
cursorObj.execute(query3)

conn.commit()
conn.close()

