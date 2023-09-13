from json import load
with open("rest.json",'r',encoding='UTF-8')as f:
    data=load(f)
# print(len(data))


# print all country names
# all_coun_name=[c.get("name") for c in data]
# print(all_coun_name)

# print all region name
# all_reg={c.get("region") for c in data}
# print(all_reg)

# print asian country names

# for c in data:
#     if c.get("region")=="Asia":
#         print(c.get("name"))

# asian_coun=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_coun)


# print population of afganisthan

# popu_afgani=[c.get("population") for c in data if c.get("name")=="Afghanistan"]
# print(popu_afgani)

# indian borders

# ind_bor=[c.get("borders") for c in data if c.get("name")=="India"]
# print(ind_bor)
# [0] if for remove double list
# items=[["cofee"]]
# print(items[0][0])
# numbers=[[1,23]]
# print(23 in numbers[0])
#
# ind_bor=[c.get("borders") for c in data if c.get("name")=="India"][0]
# print(ind_bor)
# country_border_names=[c.get("name") for c in data if c.get("alpha3Code") in ind_bor]
# print(country_border_names)


# alpha3code print meand ind=india



# print currency code of india




#
# curr_code=[c.get("code")for c in data if c.get("currencies")=="India"]
# print(curr_code)


# country with highest population
# high_pop=max(data,key=lambda u:int(u.get("population")))
# print(high_pop.get("name"))


# armstrong
# num=123
#
# # cnt=len(str(num)
# sum=0
#
# while(num!=0):
#     digit=num%10
#     sum=sum+digit
#     num//=10
# print(sum)
#
# num=153
#
# cnt=len(str(num))
# sum=0
#
# while(num!=0):
#     digit=num%10
#     sum=sum+digit**cnt
#     num//=10
# print(sum)


# 6
# 66
# 666
# 6666
# 66666
# 666666

# num=4
# for row in range(1,num+1):
#     print(str(num)*row)


# num=6
# start=1
# while(start<=num):
#     print(str(num) * start)
#     start+=1


# prime
# num=12
# is_prime=True
# for i in range(2,num):
#     if (num%i==0):
#        is_prime=False
#        break
# if(is_prime==True):
#     print(num,"is prime")
# else:
#     print(num,"is not prime")

# HCF GCD NUM1=12 NUM2=24 GCD MEANS EE 2 NUMERNAYUM DIVIDE CHEYAN PATUNA LARGEST NUMBER here it is 12
# num1=24
# num2=12
# hcf=1
# for i in range (1,(num1+1)):
#     if((num1%i==0)and(num2%i==0)):
#         hcf=i
# print(hcf)

# lcm least common factor
# num1=24
# num2=12
# hcf=1
# for i in range (1,(num1+1)):
#     if((num1%i==0)and(num2%i==0)):
#         hcf=i
#
# lcm=(num1*num2)/hcf
# print(lcm)
# print(hcf)

# # pattern
# 111
# 222
# 333
# for i in range(1,4):
#     for j in range(1,4): #here first row working 111 times col annd loop out and next row 222 if j =5 then op be 1111 2222 3333
#        print(i,end=" ")
#     print()

# 123
# 123
# 123
# for i in range(1,4):
#     for j in range(1,5):
#        print(j,end=" ") # here if i= 5 then 123 123 123 123  like wise if j=5 then 1234 1234 1234
#     print()

#
# for i in range(1,4):
#     for j in range(1,5):
#        print("*",end=" ")
#     print()

# pyramid

# for i in range(1,4):
#     for j in range(i):
#        print("*",end=" ") # ethra thavana row work avun athra thavana col work avannam so col in range of row
#     print()

#

#     # 1
#     # 12
#     # 123
# for i in range(1,6):
#     for j in range(i):
#        print(j+1,end=" ")
#     print()
# or

# for i in range(1,6):
#     for j in range(1,i+1):
#        print(j,end=" ")
#     print

# inverted pyramid
# for i in range(5,0,-1):
#     for j in range(i):
#        print("*",end=" ")
#     print()

# functions
# def addition(n1,n2):
#     res=n1+n2
#     return res
# print(addition(10,12))


# def addition(n1,n2):
#     return n1+n2
# print(addition(10,22))


# create max2 with 2 parameter return largest number
# def max_2 (n1,n2):
#     if n1>n2:
#         return n1
#     else:
#         return n2
# print(max_2(12,33))

# terrnary operation

# num=10
# print("+ve" if num>0 else "-ve")
#
# print("odd" if num%2!=0 else "even")

# num1=10
# num2=30
# print(num1 if num1>num2 else num2)
#
# def max_2 (n1,n2):
#     return n1 if n1>n2 else n2
# print(max_2(5,6))

# max of 3 numbers
# def max_3(n1,n2,n3):
#     if((n1>n2) and (n1>n3)):
#         return n1
#     elif n2>n3:
#         return n2
#     else:
#         return n3
# print(max_3(2,3,4))

# def max_3(n1,n2,n3):
#     return n1 if (n1>n2) and (n1>n3) else n2 if (n2>n3) else n3
# print(max_3(2,3,4))

#
# max=lambda n1,n2,n3:n1 if (n1>n2) and (n1>n3) else n2 if (n2>n3) else n3
# print(max(2,4,5))

# smart subtraction
# def smart_sub(n1,n2):
#     if n1>n2:
#         return n1-n2
#     else:
#         return n2-n1
#
# print(smart_sub(3,2))

# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# n1=int(input("enter a number"))
# n2=int(input("enter a number"))
# print(smart_sub(n1,n2))
#
# sub=lambda n1,n2:n2-n1
# print(sub(2,3))

# factorial
# def factorial(n):
#     fact=1
#     for i in range(1,(n+1)):
#         fact*=i
#     return fact
# print(factorial(3))

#
# prime
# def prime(n):
#     is_prime=True
#     for i in range(2,n):
#         if(n%2!=0):
#             is_prime=False
#             break
#     return "non prime number" if is_prime==True else " prime"
# print(prime(17))


# lambda its used to decrease the sixe of cade its a anomyas fn we create it by delete the fn name def return in def fn

# square=lambda num:num**2
# print(square(4))
# here square is a function
# hollow pyramid
# for i in range(1,5):
#     for j in range (1,8):
#         if((i==4)or(i+j==5)or(j-i==3)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# # inverted hollow pyramid
# for i in range(1,5):
#     for j in range (1,8):
#         if((i==1)or(i==j)or(j+i==8)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# collections to hold more than 1 object
# list,set,tuple,dictionary,number, string
# array type same size fixed more than 1 object assign


# questions
# store multiple object reference by same variable
# define
# is it possible to assign diff type of object
# duplicate allowed/
# mutable/change
# length fixed or not


# # list
# define []
# length dynamic means not fixed
# duplicates are allowed
# diff type of obj can store
# insertion order preserved yes --means same order the op be
# mutable means can change object
# colors=["red","green","green",12,10.3,True]
# print(colors[5])



# colors=["red","green"]
# for i in range(len(colors)):
#     print(colors[i])

# membership operators without range
# colors=["red","green"]
# for c in colors:
#       print(c)

# expence=[12,33,42]
# for exp in expence:
#     if exp>15:
#         print(exp)
# max_exp=max(expence)
# sum_exp=sum(expence)
# print(sum_exp)
# print(max_exp)


# arr[2,3,4] op be [7,6,5] means result be sum minus value
# arr=[2,3,4]
# op=[]
# total=sum(arr)
# for num in arr:
#     res=total-num
#     op.append(res)
# print(op)

#
# num=[2,3,4,5,6,7,9]
# evens=[]
# odds=[]
# for n in num:
#     evens.append(n) if n%2==0 else odds.append(n)
# print(evens)
# print(odds)

# users=["sachin","kohli","sheweng","rahul"]
# print("sachin" in users)

# sachin_follwers=["kohli","rahul"]
# frequently_suggest=[]
# for num in users:


#     insert[a,b]
#  a be position and b be value

# lst=[2,3,4]
# lst.insert(1,8)
# print(lst)


# user giving lemgth amd after that adding values
# emplist=[]
# length=int(input("enter the length of list:"))
# for i in range(length):
#     num = int(input(f'enter {i}th posithion element:'))
#     emplist.append(num)
# print(emplist)
#
# # adding new element to list at 2nd position which is maximum of list plus 10
# maximum=max(emplist)
# emplist.insert(2,maximum+10)
# print(emplist)


# check perticular element in list if it in that list then rename else insert another element
# stud_name=[]
# length=int(input("enter the length of list:"))
# for i in range(length):
#     name = input(f'enter {i}th posithion element:')
#     stud_name.append(name)
# ch_name=input("enter the check name:")
# for s in range(length):
#     if (stud_name[s]==ch_name):
#         stud_name[s]="anamika"
#         break
#     elif(s==length-1):
#         stud_name.insert(0,"amal")
# print(stud_name)

# duplicates find and make change
# stud_name=["a",'b','c','a']
# flag=0
#
# ch_name=input("enter the check name:")
# for i in range(len(stud_name)):
#     if (stud_name[i]==ch_name):
#         stud_name[i]="anamika"
#         flag=1
#
# if(flag==0):
#         stud_name.insert(0,"amal")
# print(stud_name)


# remove elements
# birds=["peacock","duck",'hen']
# # for i in range (len(birds)):
# #     birds.remove(birds[0])
# #     print(birds)
#
# # for i in range (len(birds)-2):
# #     birds.remove(birds[i])
# # print(birds)
#
#
# ch_bird=input("enter a bird:")
# for i in birds:
#     if i==ch_bird:
#         birds.remove(i)
# print(birds)

# stack
# ist=[]
# ist.append(9)
# ist.append(6)
# print(ist)
# ist.pop()
# print(ist)
# ist.pop()
# print(ist)


# queue

# queuee=[]
# queuee.append(9)
# queuee.append(5)
# print(queuee)
# queuee.pop(0)
# print(queuee)
# queuee.pop(0)
# print(queuee)



# ist=[5,3,4,5,5,66]
# # x=3
# # if x in ist:
# #     print("3 is present")
# # else:
# #     print("not present")
#
# x=66
# if x not in ist:
#     print("not present")
# else:
#     print("present")

# finding letters
# cars=["lambordiri","swift","porshe"]
# car_o=[]
# for i in cars:
#     if "o" in i:
#         car_o.append(i)
# print(car_o)


# remove first and 3 rd element
# ist=[5,6,7,8,9]
# ist.pop(0)
# ist.pop(2-1)
# print(ist)

# nested if


# lst=[1,2,3,4,5,6,7,8,9,55,50,54,15,20,25,30,35]
# newlst=[]
# for i in lst:
#     if i%5==0 and i%2!=0:
#         newlst.append(i)
# print(newlst)
#
# maxlst=lst[0]
# for l in lst:
#     if maxlst<=l:
#         maxlst=l
#
#
# print(maxlst)
# k=lst.remove(maxlst)
# print(lst)

# algorithm linear apporach increase complexity and uses 2 loop not good so go for without using 2 loops 2 nexted loop
#
# this for sorted elements
# lst=[2,3,4,5]
# lst2=[3,2,9,8]
# count=1
# for n1 in lst:
#     for n2 in lst2:
#         if(n1==n2):
#             print(n1)
#         count+=1
# print
#
# lst=[2,3,4,5]
# lst2=[3,4,8,9]
# (p1,p2)=(0,0)
# while(p1<len(lst) and p2<len(lst2)):
#     if(lst[p1]==lst2[p2]):
#         print(lst[p1])
#         p1+=1
#     elif (lst[p1]<lst2[p2]):
#         p1+=1
#     elif (lst[p1] >lst2[p2]):
#         p2 += 1


# all functions are defined in builtins.py file as utility functions and classes defined there max,min,sum etc are functions
# and list set dict tuple are classes and append insert pop etc are their methods defined inside class so we call it as .append
# if we want to get all methods and attributes defined in class by using print(dir(list)) etc like wise we get


# linaer apporach
# lst=[2,3,4,7,8]
# sum=7
# count=1
# for i in lst:
#     for j in lst:
#         if((i!=j) and (i<j)):
#             cur_sum=i+j
#             if(cur_sum==sum):
#                 print(i,j)
#             count+=1
#  print(count)


# best method is after sorting withput itteraction compare with pointers indexing this is for get 1 pair
# lst=[2,3,4,5,6,7,1]
# sum=6
# low=0
# upp=len(lst)-1
# count=1
# while(low<upp):
#     cur_sum=lst[low]+lst[upp]
#     if(cur_sum==sum):
#       print("pairs",lst[low],lst[upp])
#       break
#     elif (cur_sum<sum):
#          low+=1
#     elif(cur_sum>sum):
#          upp-=1
#     count+=1
# print(count)

# # this is for get all pair
# lst=[1,2,3,4,5,6,7]
# sum=6
# low=0
# upp=len(lst)-1
# count=1
# while(low<upp):
#     cur_sum=lst[low]+lst[upp]
#     if(cur_sum==sum):
#       print("pairs",lst[low],lst[upp])
#       low+=1
#     elif (cur_sum<sum):
#          low+=1
#     elif(cur_sum>sum):
#          upp-=1
# #     count+=1
# # print(count)

# find missing consequtive element from sorted list
# lst=[1,2,3,4,5,8]
# for i in range(0,len(lst)):
#      if lst[0]!=1:
#          print(1,'is missing')
#          break
#      else:
#           elem1=lst[i]
#           elem2=lst[i+1]
#           if elem2-elem1!=1:
#               print(elem1+1,"is missing")
#               break


# find duplicate element from the list
# lst=[2,3,3,4,4,5,6]
# for i in range(0,len(lst)):
#     elem1=lst[i]
#     elem2=lst[i+1]
#     if elem1==elem2:
#         print(elem1,"is dupliacte")
#         elem1+=

# lenear search object number increase itteration increase cause for complexity so go for binary algo
# lst=[2,3,4,6]
# elem=6
# is_found=False
# for i in range(0,len(lst)):
#     if elem==lst[i]:
#         is_found=True
#         break
# print("found" if is_found==True else "not found")



# binary search algorithm
# lst=[2,3,4,5]
# elem=5
# is_found=False
# low=0
# upp=len(lst)-1
# while(low<=upp):
#
#    mid=(low+upp)//2
#    if elem==lst[mid]:
#         is_found=True
#         break
#    elif elem>lst[mid]:
#        low=mid+1
#    elif elem<lst[mid]:
#        upp=mid-1
#
# print("found" if is_found==True else "not found")

# list comprehension
#
# lst=[3,4,5,8,27]
# # for num in lst:
# #     if num%2==0:
# #         print(num)
#
# odds=[num for num in lst if num%2==0]
# print(odds)
#
# num_gr_five=[num for num in lst if num>5]
# print(num_gr_five)


# cubes=[i**3 for i in range(20)]
# print(cubes)

# # print all numbers divisible by five
# div_five=[num for num in lst if num%3==0]
# print(div_five)

# nested nest  inside one list another list
# lst=[
#     [2,3,4],
#     [3,4,5],
#     [2,1]
#     ]
# for sub in lst:
#     for num in sub:
#         if num>4:
#
#            print(num)


# all_num=[num for sub in lst for num in sub]
# print(all_num)

# all_num_gr_5=[num for sub in lst for num in sub if num>3]
# print(all_num_gr_5)

#
# mobiles=[
#     [100,"redmi",23000,"5g"],
#     [101, "galaxy", 32000, "5g"],
#     [102, "oneplus", 42000, "5g"],
#     [103, "notepad", 133000, "5g"],
#     [104, "nokia", 13000, "4g"],
#     [105, "samsung", 25000, "3g"],
#     [106, "vivo", 42000, "5g"]
#
# ]
# total_num_mobile
# print(f'{len(mobiles),"mobiles available"}')

# print all mobile name
# for mob in mobiles:
#     print(mob[1])


# mob_names=[mob[1] for mob in mobiles]
# print(mob_names)

# print only 4g network mobile name
# mob_4g=[mob[1] for mob in mobiles if mob[3]=="4g"]
# print(mob_4g)

# print mob name price less than 30000
# mob_pric_ls=[mob[1]for mob in mobiles if mob[2]<30000]
# print(mob_pric_ls)

# print mob name available in range between 30000 to 50000
# mob_pric_ls=[mob[1]for mob in mobiles if mob[2]<50001 and mob[2]>30000]
# print(mob_pric_ls)

# mob_pric_ls=[mob[1]for mob in mobiles if mob[2] in range(30000,50001)]
# print(mob_pric_ls)
#
# mob_pric_ls=[mob[1]for mob in mobiles if 30000<mob[2]<50001]
# print(mob_pric_ls)

# print all 5g mobile names available under 25000
#
# mob_5g_pric_ls=[mob[1] for mob in mobiles if mob[3]=="5g" and mob[2]<25000]
# print(mob_5g_pric_ls)

# set works


# st={} this is dict means no value so its dict not empty set
# st=set() # create empty set
# st={2,3,4} # this is set

# dupliactes are not allowed all elements are unique
# insertion order is not preserved just opposite to list so we cant use indexing in set ranging not possible

# set is mutable
# st={3,4,5}
# for el in st:
#     print(el)

# adding elememt by add method not by append
# st={3,4,5}
# st.add(23)
# print(st)

# dupliacte remove in list by using set  converting list to set
# lst=[3,3,4,5,4]
# st=set(lst)
# print(st)

# set opeation union set_diff intersection
# union combin both
# st1={5,6,6,7}
# st2={6,9,4,4}
# uni_set=st1.union(st2)
# print(uni_set)

# intersection means common
# inter_st=st1.intersection(st2)
# print(inter_st)

# difference onil ulladh ninn matiya set ele remove
# diff_st=st1.difference(st2)
# print(diff_st)

# remove for ele remove
# alluser=["lal","vijay","nivin","dq","asif"]
# dq_frdlist=["lal","vijay"]
# asif_frdlist=["lal"]

# sugg_dq=set(alluser).difference(dq_frdlist)
# sugg_dq.remove("dq")
# print(sugg_dq)

# mutal
# mutal_asif=set(dq_frdlist).intersection(set(asif_frdlist))
# print(mutal_asif)

# text="morning"
# vowels={"a","e","i","o","u"}
# v_count=0
# c_count=0
# for ch in text:
#     if ch in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)

# set is mutable it can update with another set not by element not by indexing

# set update
# st1={1,3,4}
# st2={3,4,5}
# st1.update(st2)
# print(st1)
# tuple
#preserved order so indexing
# duplicate value allowed
# tuple()
# tp=()
# tp=(1,2,3,"reethu",False)
# print(tp)
# print(type(tp))
# print(tp[0])

# tuple cant update means inmutable not modify this is only diff compare with list
# if tuple have only one value then it represent as list so a "," is added then it call as tuple tp=(1,)
# tuple is use when the data required no updattion in case of data accessing from a file import data


# dictionary {key:value} duplicate key is not possible values are possible
# emp={"name":"hari","salery":450}
# print(emp["salery"])

# for key in emp:
    # print(key)
    # print(key,emp[key])

# adding new elements
#
# emp["gender"]="male"
# print(emp)

# # updating
# emp["gender"]="female"
# print(emp)

# emp["salery"]+=2000
# print(emp["salery"])

# check existance of key
# if ("name" in emp):
#     print("present")
# else:
#     print("not present")

# dictionay there is no method defined


# find the first recurrsive element in givin list after that find the count of all letters

# text="ABABC"
# wc={}
# for ch in text:
#     if ch in wc:
#         print(ch,"is first recurssive character")
#         break
#     else:
#          wc[ch]=1

#
# text="ABABC"
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#          wc[ch]=1
# print(wc)


# values only take by  values() as list [], keys only keys()  items() will return both keys and values in
# tuple format key vech value aa edukan get method get(key)
# emp={"name":"hari","salery":450}
# print(emp.values())
# print(emp.keys())
# print(emp.items())
# for k,v in emp.items():
#     print(k,v)

# print(emp["name"]) server got stop execution when an in valid key is defined but when use get method the server
# not stop execution its its non e and then proceessed futher program
# print(emp.get("name"))
# print("reethu")


# remove key value pair pop(key)


# emp.pop("name")
# print(emp)


# get the count of frame amd library
# dataa={
#     "django":"frame",
#     "vue":"frame",
#     "ajax":"library",
#     "react":'library'
#     }
# wcs={}
# for v in dataa.values():
#     if v in wcs:
#         wcs[v]+=1
#     else:
#         wcs[v]=1
# print(wcs)


# get op as {"frame":["django","vue"],"library":["ajax","react"]}
# wcs={}
# for k,v in dataa.items():
#     if v in wcs:
#         wcs[v].append(k)
#     else:
#         wcs[v]=[k]
# print(wcs)

#
# text="AAABBCCCCCCDD"
# # FIND MOST RECURSSIVE ELEMENT
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#         wc[ch]=1
# print(wc)
# print(max(wc,key=lambda key:wc.get(key)))
# print(min(wc,key=lambda k:wc.get(k)))


# def get_val_key(key):
#     return wc.get(key)
# print(get_val_key("A"))

# std={"roll":12,"name":"reethu","course":"python"}
#
# def get_id(st):
#     return st.get("roll")

# get_id=lambda st:st.get("roll")


# def get_name(st):
#     return st.get("name")

# get_name=lambda st:st.get("name")


# def get_course(st):
#     return st.get("course")

# get_course=lambda st:st.get("course")

# print(get_name(std))
# print(get_course(std))
# print(get_id(std))

# args include so many variables type is tuple positional argument takes any number of parameter type tuple
# type is class max min sum all are bulit in functions
# def add(*args):
#     print(args)
#
# add(10)
# add(10,20,30)

# lst=[3,4]
# print(sum(lst))

# def summs(*args):
#     return sum(args)
#
# print(summs(3,6,8))


# summ=lambda *args:sum(args)
# print(summ(3,4,5,6))

# maxii=lambda *args:max(args)
# print(maxii(8,7,6))

# words=["hello","hai","good","morg","aaaaaanjdfhfsvs"]
# if we take max() then we get op as morg means they take based on alphabet order  min then a max then z start so
# if we want to get the longest word then we use
# def max(*args,key=none) this is default we can edit it
#
# def get_len(w):
#     return len(w)
#
# print(max(words,key=get_len))

#
# print(max(words,key=lambda w:len(w)))
# print(sorted(words,key=lambda w:len(w)))
# print(sorted(words,key=lambda w:len(w),reverse=True))


# print(min(words, key=lambda w:len(w)))

# sorted

# list inside it methods sort and sorted function available like print

#
# lst=[3,4,5,1]
# print(sorted(lst))
# print(sorted(lst,reverse=True))
#
# def sorted(*args,**kwargs)
#
# movies={"mystory":2,"kgf":5,"popins":4,"sea":3}
# print(movies.keys())

#
# print(max(movies,key=lambda k:movies.get(k)))
# print(sorted(movies,reverse=True,key=lambda k:movies.get(k)))



















































