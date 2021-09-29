import sqlite3
Database = sqlite3.connect("schooltest.db")
curschool = Database.cursor()
print("Enter the name for whom you wish to delete ")
name = input()
# try:
curschool.execute("DELETE FROM student WHERE name = (?);",(name,))
Database.commit()
print("Deletion operation successfull.")
# except:
    # print()
    # Database.rollback()
# finally:
Database.close()
