from json import load
with open("movie.json",'r',encoding='UTF-8')as m:
    dat=load(m)
print(dat)
# length of movies
print(len(dat))
# print all movie names
movnames=[u.get("title") for u in dat]
print(movnames)
# print movie with highest run time
highrun=max(dat,key=lambda u:int(u.get("runtime")))
print(highrun.get("title"))
# print all geners set is for remove duplicates
genre={g for m in dat for g in m.get("genres")}
print(genre)

#print movies with genre comedy
genre=[m.get("title") for m in dat if "Comedy" in m.get("genres")]
print(genre)


# print movie with genre comedy or fantacy
genre_fan_com={m.get("title") for m in dat for g in m.get("genres") if g in ["Comedy","Fantasy"]}
print(genre_fan_com)


# year wise movie count
yc={}
for m in dat:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
print(yc)

# find max movie released year
# names=["name1":"hari"] we want to get hari by names.get(name1)
print(max(yc,key=lambda k: yc.get(k)))
print(min(yc,key=lambda k: yc.get(k)))



