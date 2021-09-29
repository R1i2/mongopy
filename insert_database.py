import sqlite3
Database1 = sqlite3.connect("schooltest.db")
curschool = Database1.cursor()
data = {
    1:{
        "name":"Hermoine Granger",
        "house":"Gryfindor",
        "age":21,
        "marks":20
    }, 
    2:
    {
        "name":"Harry Potter",
        "house":"Gryfindor",
        "age":22,
        "marks":100
    },
    3:
    {
        "name":"Malfoy",
        "house":"Slytherin",
        "age":20,
        "marks":100
    }
}
curschool.execute("INSERT INTO student(STUDENTID, name, age, marks) VALUES (2,'Dumbledore',59,89);")
Database1.commit()
# for i,j in data.items():
#     curschool.execute("INSERT INTO student (STUDENTID, name, age, marks) VALUES (?,?,?,?)",(i+2,j['name',     #j['age'],j['marks']))
#     Database1.commit()
Database1.close()