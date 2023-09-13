import mysql.connector

def connect_db(host="localhost", user="root", password=None, port=3306,database=None):
    db=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database,





    )
    return db
