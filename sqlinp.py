import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="reginarinshy143@R", port=3306,
                               database="animal")

cursor = db.cursor()
query = """
insert into pets(age,gender,breed,location,price) values(19,'female','breed3','pkd',87981)


"""
cursor.execute(query)
db.commit()#save changes