import sqlite3
Database = sqlite3.connect("schooltest.db")
curschool = Database.cursor()
name = input("Enter name of the student: ")
marks = int(input("Enter new marks: "))
query = "UPDATE student SET marks = (?) WHERE name= (?);"
try:
    curschool.execute(query,(marks,name))
    Database.commit()
    print("Data successfully updated")
except:
    print("Error in operation")
    Database.rollback()
finally:
    Database.close()