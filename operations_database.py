import sqlite3
print("Enter the name of database:")
name_of_database = input()
Database = sqlite3.connect(name_of_database)
cursor = Database.cursor()
def create_table():
    print("Enter the name of the table: ")
    table_name = input()
    query = "CREATE TABLE "+table_name+" (HOTELID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT(20) NOT NULL, minPrice INTEGER);"
    cursor.execute(query)
    Database.commit()
def insert_record(count):
    while(count):
        print("Enter the id of hotel: ")
        unique_id = input()
        print("Enter the name of the hotel: ")
        name = input()
        print("Enter minPrice for two people")
        minPrice = input()
        print("Enter the name of the table: ")
        table_name = input()
        query = "INSERT INTO "+table_name+" (HOTELID, name, minPrice) VALUES (?,?,?);"
        try:
            cursor.execute(query,(unique_id,name,minPrice))
            Database.commit()
            print("Insertion successs.")
        except:
            print("Insertion unsuccessfull.")
            Database.rollback()
        finally:
            count = count - 1
def update_record():
    print("Enter the name of Hotel: ")
    name = input()
    print("Enter the new Price: ")
    minPrice = int(input())
    print("Enter the name of the table: ")
    table_name = input()
    query = "UPDATE "+table_name+ "SET minPrice = ? WHERE name = ?;"
    try:
        cursor.execute(query,(minPrice,name))
        Database.commit()
        print("Update success.")
    except:
        Database.rollback()
        print("Update unsuccessfull")
def delete_record():
    print("Enter the name of Hotel: ")
    name = input()
    print("Enter the name of the table: ")
    table_name = input()
    query = "DELETE FROM "+table_name+" WHERE name = ?;"
    try:
        cursor.execute(query,(name,))
        Database.commit()
        print("Deletion success.")
    except:
        Database.rollback()
        print("Deletion unsuccessfull")
def fetch_record():
    print("Enter the name of the table: ")
    table_name = input()
    query  = "SELECT * FROM "+table_name+";"
    cursor.execute(query)
    records = cursor.fetchall()
    for rec in records:
        print(rec)
    print ("\n"*3)
create_table()
fetch_record()
insert_record(5)
fetch_record()
update_record()
fetch_record()
delete_record()
fetch_record()
Database.close()


