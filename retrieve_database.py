import sqlite3
Database = sqlite3.connect("schooltest.db")
query = "SELECT * FROM student;"
curschool = Database.cursor()
curschool.execute(query)
while(True):
    record = curschool.fetchone()
    if record == None:
        break
    print(record)
curschool.execute(query)
result = curschool.fetchall()
for record in result:
    print(record)
Database.close()