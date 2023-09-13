movies=[

    {"name":2018,"genre":["mystery","comedy"],"rating":8,"language":"mala","year":2011},
    {"name": "vhgsM", "genre": ["fantasy"], "rating": 9,"language":"tamil","year":2017},
    {"name": "ammu", "genre": ["mystery"], "rating": 6,"language":"hindi","year":2023},

    {"name": "appu", "genre": ["history"], "rating": 7,"language":"mala","year":2018}

]



# print all using map
# item_names=list(map(lambda it:it.get("name"),movies))
# print(item_names)
# item_nam=[i.get("name") for i in movies]
# print(item_nam)

# map price
# map_price=list(map(lambda it:it.get("language"),movies))
# print(map_price)


# filter based language =mala
# filter_lang=list(filter(lambda m:m.get("language")=="mala",movies))
# print(filter_lang)

# filters=[m.get("name") for m in movies if m.get("language")=="mala"]
# print(filters)
# for m in movies:
#     print(m.get("name"))
# movie_names=[m.get("name") for m in movies]
# print(movie_names)

#    filter movie genre=mystery
# for m in movies:
#     if "mystery" in m.get("genre"):
#         print(m.get("name"))
# mys_movie=[m.get("name") for m in movies if "mystery" in m.get("genre")]
#
# print(mys_movie)

# highest rating based
# rat=max(movies,key=lambda m:m.get("rating"))
# print(rat.get("name"))

# yearfilter
# for m in movies:
#     if m.get("year")==2023:
#         print(m.get("name"))
# year_filter=[m.get("name") for m in movies if m.get("year")==2023]
# print(year_filter)

# sorting based on rating
# rat_sort=sorted(movies,key=lambda m:m.get("rating"),reverse=True)
# print(rat_sort)

# mala_move=[m.get("name")for m in movies if m.get("language")=="mala"]
# print(mala_move)




# temper=[
#     {"tvm":23},
# {"tcr":24},
# {"tvm":28},
# {"ktm":27},
# {"ktm":29},
# {"tcr":22},
# {"tvm":29},
#     ]
# temp={}
# for t in temper:
#     for k,v in t.items():
#         dis_name=k
#         curr_tem=v
#         if dis_name in temp:
#             old_temp=temp[dis_name]
#             if curr_tem>old_temp:
#                 temp[dis_name] = curr_tem

#
#         else:
#              temp[dis_name]=curr_tem
#
# print(temp)


# items=[
#
#     {"cofee": 30},
#     {"suge": 40},
#     {"munce": 50},
#
#     {"diare": 20}
#
# ]
# offers=[
# {"cofee": 10},
#     {"suge": 20},
#     {"munce": 30}
#
# ]

# print todays selling price



# map and filter both are class if condition indakil filter other wise map map and filter in builtin file reduce in funtool file
# ella object ill oru fnction applay cheya map
# condition indakil filter
# reduce process cheidh only one output ex:higest total std like that

# lst=[4,5,6]
#
# # map(function,iterabel)
# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)
# lst_sq=[n**2 for n in lst]

# squares=list(map(lambda num:num**2,lst))
# print(squares)

#filter() condition true ayyit veruna full return cheyum
# def is_even(n):
#     return n%2==0
# evenss=[n for n in lst if n%2==0]

# evenss=list(filter(lambda num:num%2==0,lst))
# print(evenss)

# print all greater than 3
# graet_three=list(filter(lambda num:num>4,lst))
# print(graet_three)

# reduce()


# identifiers  variable name,function name,class name
# flow control interpetted annu python line by line procecution
# no need of explicit in python age 12 int enn paranj kodukanda so python is dynamically typed
# python if age='hello' srring ayyit qutomatically convert avum in case of python so dynamically typed

# string
# word="heLLO3ammalike"
# print(word.capitalize())
# print(word.count("L"))
# print(word.split(" "))  # spilt(*args)
# print(word.casefold())
# print(word.find("L"))
#
# # startswith return bullean  endswith return boolean
#
# print(word.startswith("he"))
# print(word.endswith("ke"))
#
# print(word.isalpha())   #Space be there so false only alphabet then true
# print(word.isdigit())
# print(word.isalnum()) # alphabet or numeric then true

#
# text="one 100 and fifty 5"
# sp=text.split(" ")
# print(sp)
# di=[]
# for i in sp:
#     if i.isdigit()==True:
#         di.append(i)
# print(di)

# for i in sp:
#     if i.isdigit():
#         print(i)

#
# dig=[w for w in text.split(" ") if w.isdigit()]
# print(dig)

# text="reethu is A good girl and"
# print words that starts with vowels
# vow={"a","e","i","o","u"}
# tt=text.casefold()
# kk=text.split()
# for i in kk:
#     if i[0].casefold() in vow:
#        print(i)

#
# ws=[w for w in text.split() if w[0].casefold() in vow]
# print(ws)

# text="heloo im in ahrissur"
# # print longest word
# tt=text.split()
#
# print(max(tt,key=lambda m:len(m)))
#
# wc={}
# for w in tt:
#     if w not in wc:
#         wc[w]=len(w)
# print(wc)

# text="heloo im in ahrissur"
# tt=text.split()
# bb=text.startswith("heloo")
# if bb==True:
#     print("sentence starts with hello")

# if tt[0]=="heloo":
#     print("sentence starts with hello")

# regular expression as re in buit annu ^ starts with check cheya "carrot" sympol here we can find all using search method
# start end where there it we can find using one expression
# in case of end find by using doller sign at end
# .* means in between anything come not bother
# import re

# text="heloo im in ahrissur reethu"
# x=re.search("^heloo",text)
# y=re.search("im",text)
# z=re.search("reethu$",text)
# st_end=re.search("^heloo.*reethu$",text)
# st_end2=re.search("^heloo.*in",text)
# print(st_end2)
#
#
#
# print(st_end)
# # print(z)
# # print(x)
# print(y)

#mobile number indian or not

# import re
# mob=input("enter you mob number:")
# x=re.search("^[+]91",mob)
# if(x):
#     print("number is indian")
# else:
#     print("number is foregin")

# import re
# resi=input("enter you resi num:")
# ekm=re.search("^0484",resi)
# tcr=re.search("^0487",resi)
# ktm=re.search("^0488",resi)
# if ekm:
#     print("number in ekm")
# elif tcr:
#     print("tcr")
# elif ktm:
#     print("ktm")
# else:
#     print("invlid")


# count words where all this hi come that can count [0-5] get first value
import re
# texts="hi hai hi hloo hi 48:49 hi hi 13:68,90 hide 70 inhile reethu"
# sent="hi hide inhile"
# st=re.findall("hi",sent)
# print(len(st))
#
# ct=texts.count("hi")
# print(ct)
# di=re.findall("[0-5][0-9]",texts) # we want to get value less than 60 so 0-5 indicate digit and 0-9 indicate last digi
# print(di)

# verify a gmail account
# import re
# gmail=input("enter your gmail:")
# g=re.search("@gmail.com$",gmail)
# if g:
#     print("valied")
# else:
#     print("invalid")


# multiple times reapeat cheyundoo check cheyan
# import re
# text="aaaabbbbc"
# text1="abababa"
# t5=re.search("[a-z]{4}",text)
# t=re.search("[a]{4}",text)
# t1=re.search("[a]{4}",text1)
# t3=re.search("[b]{4}",text)
# print(t)
# print(t1)
# print(t3)
# print(t5)

# te="abcd4626"
# t6=re.search("[a-z]{4}",te) # contious alphabet
# print(t6)

# mobile digit varification

# import re
# mob=input("enter you mob number:")
# x=re.search("^[+]91.*[1-9]{10}",mob)
# if(x):
#     print("number is valied indian")
# else:
#     print("number is invalid")

# position and order is imp
# stru="34abABCDEE70998"
# s=re.search("[a-z]{2}[A-Z]{4}",stru)
# print(s)

# substitute endhakillum replace cheidh vera vekyan sub()
# import re
# stri="hello all how are you"
# s=re.sub(" ",",",stri)
# print(s)

from re import *

# this means import all (*)from re finditer itterate object regular expression used for pattern matching cases
# start is for get position and group is for get that product
# [ab] means either a or b
# [a-c] from a to c
# [a-zA-Z] from both cap ans small a to z
# [0-9] for digit [] this means take all
# [^a] means except a means a indavv illya
# to take only special chara means [^a-zA-Z0-9]
# a-z   =   /w for all alphas
# 0-9  =   /d
# A-Z  =   /W
# SPACE  =  /s
# EXCLUDE SPACE  =/S
# EXCLUDE DIGITS  ==[^0-9]    =   /D



# QUANTIFIERS
# a*  means any number of a == aa    a indavum indavatha erkkamm
# mobile 91 indavam indavatha erekam * meaning
# a{2}   == a 2 times
# a{2,3}  == a min 2 max 3



# texts="luminar is luminar and"
# matcher=finditer("luminar",texts)
# print(matcher)
# count=0
# for m in matcher:
#       print(m.start())
#       print(m.group())
#     count+=1
# print(count)
#
#  from re import *
# tt="AAJLD78687098%*&**)"
# mat=finditer("[^a-zA-Z0-9]",tt)
# print(mat)
# for m in mat:
#     print(m.group())

# python chara start with k=m
# second chara should be digit and its divisible by 3
# any num of chara

# var_name="k6f0"  this is valied
# rule="[k-m][369][^a-zA-Z0-9]*"  #* this for ethra ennam vennam enkillum veram vann illyakillum korappam illya
#
# from re import *
# var_name="NUM_1"
# rule="[k-m][369][a-zA-Z0-9]*"
# rule1="[_a-zA-Z][a-zA-Z0-9_]*"
# tt=fullmatch(rule1,var_name)
# if tt !=None:
#     print("valied")
# else:
#     print("invalid")

# java variable set start with an alphabet special chara_$ length limit 1 to 10
# from re import*
# rule2="[a-zA-z][A-Za-z$_0-9]{0,10}"
# var_name="g1$_jhjl9992"
# pp=fullmatch(rule2,var_name)
# print("valied" if pp!=None else "invalied")

# number plate kl-08-bn-4970
# rule3="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# rule6="[a-z]{2}[-][0-9]{2}[-][a-z]{2}[-][0-9]{4}" # all cases in india

# from re import*
# rule2="[a-zA-z][A-Za-z$_0-9]{0,10}"
# var_name="kl-48-bn-6678"
# pp=fullmatch(rule3,var_name)
# print("valied" if pp!=None else "invalied")
#
#
# violations=["kl-19-av-7786",
# "kl-89-hh-9786",
# "kl-09-tn-770",
# "tn-19-av-798",
# "knl-19-avo-7786",
# "kol-19-av0-7786"]


# # valied kerala vehichl only print
# rule3="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}"
# for num in violations:
#      kk=fullmatch(rule3,num)
#      if kk!=None:
#          print(num)


# tweets="what a game ,if you happy @reethu23 @silver4568 him @"
# kk=tweets.split(" ")
# rule3="[@][a-zA-Z0-9_]*"
# for num in kk:
#      pp=fullmatch(rule3,num)
#      if pp!=None:
#          print(num)

#
# tweets="what a game ,if you happy @reethu23 @silver4568 him @"
#    # * means any number of times + means atleast one
# rule3="[@][a-zA-Z0-9_]+"
# pp=finditer(rule3,tweets)
# for m in pp:
#     print(m.group())





















