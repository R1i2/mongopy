import sqlite3
Database1 = sqlite3.connect('schooltest.db')
curschool = Database1.cursor()
curschool.execute('''CREATE TABLE student(STUDENTID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT(20) NOT NULL, age INTEGER,marks REAL);''')
Database1.close()