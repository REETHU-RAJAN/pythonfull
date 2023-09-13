# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/datsss.txt","r")
# for line in f:
#     print(line)

# other wise 2 back slach or one forward slash  \n for new line
# strip left and strip right to remove elements


# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/datsss.txt","r")
# words=[]
# for line in f:
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         words.append(w)
# print(words)

# print only unique words
# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/datsss.txt","r")
# words=[]
# for line in f:
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         if w not in words:
#             words.append(w)
# print(words)

# or

# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/datsss.txt","r")
# words=set()
# for line in f:
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         if w not in words:
#             words.add(w)
# print(words)


# print absent students from attandance list and todays list after combare


# f=open("C:\\Users\\admin\\PycharmProjects\\pythonmy\\database\\htttt\\todaysattand.txt","r")
# k=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/attandance.txt","r")
# total_std=set()
# pre_std=set()
# for line in k:
#     total_std.add(line.rstrip("\n"))
# print(total_std)
# for line in f:
#     pre_std.add(line.rstrip("\n"))
# print(pre_std)
# absent_std=total_std-(pre_std)
# print(absent_std)


# valied email
# from re import *
# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/mailsfile.txt","r")
# valied_email=set()
# rule="[a-zA-Z0-9][a-zA-Z0-9_$%&]*[@]gmail[.]com"
# for id in f:
#     id=id.rstrip("\n")
#     mat=fullmatch(rule,id)
#     if mat!=None:
#
#         valied_email.add(id)
# print(valied_email)

# vehicle valied


# from re import *
# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/vechile.txt","r")
# kerala_reg=set()
# tamil_reg=set()
# rule1="[K][L]-[0-9]{1,2}-[A-Z]{2}-[0-9]{4}"
# rule2="[T][N]-[0-9]{1,2}-[A-Z]{2}-[0-9]{4}"
# for i in f:
#     veh=i.rstrip("\n")
#     mat=fullmatch(rule1,veh)
#     if mat!=None:
#         kerala_reg.add(veh)
#
#     tmat=fullmatch(rule2,veh)
#     if tmat!=None:
#         tamil_reg.add(veh)
# print("kerala",kerala_reg)
# print("tamil",tamil_reg)


# file write
# f=open("./fwrite.txt","w")
# # f.write("override")
# language=["python","java","c","c++"]
# for i in language:
#     f.write(i+"\n")
# print("finish")

# # leap year only write to file
# f=open("./leap.txt","w")
# leaps=[2000,2010,2008,2013,2100]
# for i in leaps:
#
#     if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
#         f.write(str(i)+"\n")
# f.close()


# # 1890-3000 write to a file
# f=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/range.txt","w")
# for i in range(1890,3001):
    # f.write(str(i)+"\n")

# fread=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/range.txt","r")
# fwri=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/yerr.txt","w")
# for line in fread:
#     year=int(line.rstrip("\n"))
#     if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
#       fwri.write(str(year)+"\n")

#package means collection of python modules(norml files)

# fe=open("C:/Users/admin/PycharmProjects/pythonmy/database/htttt/listofdict.txt","r")
# users=[]
# for line in fe:
#     text=line.rstrip("\n")
#     name,followers,follings=text.split(",")
#     print(name,followers,follings)


#           # anagram
# word=input("enter aword ")
# out=input("enter aword ")
# srt_word=sorted(word)
# srt_out=sorted(out)
# if srt_word==srt_out:
#     print("anagram")
# else:
#     print("non anagram")


# using one words whaether got another word kangaroo method

# word="eagle "
# out="eggs"
#
# wc={}
# is_kan=True
# for c in word:
#     if c in wc:
#         wc[c]+=1
#     else:
#         wc[c]=1
# for ch in out:
#     if ch in wc and wc[ch]>0:
#          wc[ch]-=1
#     else:
#         is_kan =False
#         break
# print(is_kan)