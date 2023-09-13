
from json import load
with open("dat.json",'r')as f:
    dat=load(f)
print(dat)
# for u in dat:
#     print(u.get('name'))
#     print(u.get("course"))

names=[u.get("name") for u in dat]
print(names)

# student with highest mark here it is in form of dictionary

stdmax=max(dat,key=lambda s:s.get("total"))
print(stdmax)

# sort all with respect to total order by desc

sout=sorted(dat,reverse=True,key=lambda s:s.get("total"))
print(sout)

# python student names

pystd=[u.get("name") for u in dat if u.get("course")=="python"]
print(pystd)