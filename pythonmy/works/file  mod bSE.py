# #file=open("reethu.txt",'x')
# #print(open)
# file=open("reethu.txt",'w')
# file.write("iam reethu"'\n')
# file.write("iam fine"'\n')
# file.write('hope you fine''\n')
# file.close()
# file = open("reethu.txt",'r')
# print(file.read())
# file.close()
# #to copy all the data from 1 file to another
# # f="reethu.txt"
# # x="copiedfile.txt"
# # file=open(f,'r')
# # data=file.read()
# # file.close
# # with open(x,'a')as doc:
# #     doc.write(data)
# f1=open("copy_op.txt",'w')
# with open("reethu.txt",'r')as ree:
#     for i in ree:
#         f1.write(i)
# ree.close()
# #total no of words in file
# def txt_words():
#     f=open("reethu.txt",'r')
#     data=f.read()
#     cnt=0
#     w=data.split()
#     for word in w:
#         cnt=cnt+1
#     f.close()
#     print("no of letters:",cnt)
# txt_words()
# #total no of lowercase letters in file
# def lowercase_lett():
#     f=open("reethu.txt",'r')
#     data=f.read()
#     cnt=0
#     for i in data:
#         if i.islower():
#             cnt=cnt+1
#     f.close()
#     print("lowercase:",cnt)
# lowercase_lett()
# # python to convert lower to upper  case
# with open("reethu.txt",'r') as ree:
#     string=ree.read()
#     print(string)
#     for i in string:
#         x=string.upper()
#     print(x)
# ree.close()
# ##reverse lines with reverse the words in lines and store in another file
# file1=open("op file ree.txt",'w')
# with open("reethu.txt",'r') as ree:
#       words=ree.read()
# rev=words[::-1]
# file1.writelines(rev)
# file1.close()
# ree.close()
# # reach each line in a file
# file=open("reethu.txt",'r')
# for i in file:
#     print(i)
#
# # appen text to file
# with open("reethu.txt",'a') as ree:
#     ree.write('hello')
#
#seek and tell
file=open("reethu.txt",'r')
# file.seek(10)
# data=file.read()
# print(data)
line1=file.readline()
print(line1)
position=file.tell()
print(position)
file.seek(10)
print(file.tell())