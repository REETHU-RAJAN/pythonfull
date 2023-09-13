from get_connection import connect_db
db=connect_db(password="reginarinshy143@R",database="animal")
cursor=db.cursor()
query="select * from pets"
cursor.execute(query)
records=cursor.fetchall()
for rec in records:
    print(rec)
    db.close()