dict1={"name":"priya","age":12,"place":'priya',"course":"python"}
key=dict1.keys()
print(key)
value=dict1.values()
print(value)
x=[]
for i in value:
    if i not in x:
        x.append(i)
print("duplicates removed:",x)
new_dict=dict(zip(key,x))
print(new_dict)

