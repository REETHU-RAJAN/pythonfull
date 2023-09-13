import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="reginarinshy143@R",port=3306)
print(mydb)
mycursur=mydb.cursor()
#mycursur.execute("create database maypython")
# mycursur.execute("use maypython")
# mycursur.execute("create table students(name varchar(250),age int,roll_num int)")
# sql="insert into students(name,age,roll_num)values(%s,%s,%s)"
# # val=("reethu","28","1")
#
#
# # val=("ammu","23","2")
#
#
# # mycursur.execute("drop table students")
# #
# val=("paru","76","3")
# # val=("sil","55","4")
# mycursur.execute(sql,val)
# mydb.commit()
# print(mycursur.rowcount,"record inserted.")
""" inner join 
..............
it combines rows from 2 or more tables based on specified condition 
and returns only the row that having values in both tables

select colomn1,colomn2,....
from table1
inner join table 2 ON table1.colomn_name = table2.colomn_name;"""
query="create database animal"
mycursur.execute(query)






