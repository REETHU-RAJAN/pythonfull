# dictionary mutabe,ordered,duplicates are not allowed,indexed
dict1={"name":"priya","age":12,"place":'abc',"course":"python"}
print(dict1)
print(dict1["name"])
print(dict1.get("name"))
dict1['name']='aisu'
print(dict1)
dict1.update({'course':"react",})
print(dict1)
dict1.update({'quali':"btech",})
print(dict1)
#keys only
x=dict1.keys()
print(x)
#values only
x=dict1.values()
print(x)
#remove by pop
dict1.pop("name")
print(dict1)
#last item remove popitem
dict1.popitem()
print(dict1)
#copy
z=dict1.copy()
print(z)
#clear
#d=dict1.clear()
#print(d)

#setdefault
k=dict1.setdefault("course","mtech")
print(k)

# combine both key and value using zip
keys=("ten","twenty")
values=(10,20)
new_dict=dict(zip(keys,values))
print(new_dict)

#rename

dict1={"name":"priya","age":12,"place":'abc',"course":"python"}
dict1['class']=dict1.pop('course')
print(dict1)
dict1={"name":"priya","age":12,"place":'abc',"course":"python"}
dict1['firstname']=dict1.pop('name')
print(dict1)
#merge two dict into one
dict1={"name":"priya","age":12,"place":'abc',"course":"python"}
dict2={"quali":"btech"}
dict1.update(dict2)
print(dict1)
#sampledict nested dict values taken
sampledict={
    "class":{
        "students":{
            "name":"mike",
            "marks":{
                "phiysics":70 ,
                "history":80
            }
        }
    }
}
print(sampledict["class"]["students"]["marks"]["history"])
#sample dict edit in nexted iff
sampledict={
    "leap_or_not(year)dict1":{"name":"priya","age":12,"course":"python"},
    "dict2":{"place":'abc','quali': 'btech'},
    "dict3":{"job":"pytho dev"}
}
x=sampledict["dict3"]["job"]="java dev"
print(sampledict)
