from get_connection import connect_db


class petsview:
    def connect(self):
        db=connect_db(password="reginarinshy143@R",database="animal")
        return db
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from pets"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    def retrieve(self,id):
        db=self.connect()
        cursor = db.cursor()
        query = f"select * from pets where id={id}"
        cursor.execute(query)
        record= cursor.fetchone()
        return
    def post(self,*args,**kwargs):
        db = self.connect()
        cursor = db.cursor()
        query ="insert into pets (age,gender,breed,location,price)" "values(%s,%s,%s,%s,%s)"
        data=tuple(v for v in kwargs.values()) # we can use list too but list we can update(append)here there is no require of update so use tuple :tuple no updation possible
        cursor.execute(query,data)
        db.commit()
        return kwargs
    def postt(self,*args,**kwargs):
        db = self.connect()
        cursor = db.cursor()
        age=kwargs.get("age")
        breed= kwargs.get("breed")
        gender= kwargs.get("gender")
        location= kwargs.get("location")
        price= kwargs.get("price")
        data =(age,gender,breed,location,price)
        query ="insert into pets (age,gender,breed,location,price)" "values(%s,%s,%s,%s,%s)"
        # data=tuple(v for v in kwargs.values()) # we can use list too but list we can update(append)here there is no require of update so use tuple :tuple no updation possible
        cursor.execute(query,data)
        db.commit()
        return kwargs
    def destoy(self,id):
        db = self.connect()
        cursor = db.cursor()
        query = f"delete from pets where id ={id}"

        cursor.execute(query)
        db.commit()
        return "record deleted"
    def update(self,id,*args,**kwargs):

        db = self.connect()
        cursor = db.cursor()
        data = list(v for v in kwargs.values())
        data.append(id)
        query ="update pets set age=%s gender=%s breed=%s location=%s price=%s where id=%s"


        cursor.execute(query,data)
        db.commit()











pv=petsview()
#print(pv.get())
#print(pv.retrieve(2))
# print(pv.postt(age=26,gender="male",breed="breed1",location="mplm",price=68877))
# print(pv.destoy(2))
print(pv.update(id=3,age=29,gender="female",breed="breed5",location="ekm",price=68877))