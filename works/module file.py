# # create x, add a append ,write w,delete os.remove,read r
# #file = open("my file.txt",'x')
# file = open("my file.txt",'w')
#
# file.write("hi dears")
#
# file.close()
# #
# #print(open)
# file = open("my file.txt",'r')
# print(file.read())
# file.close()
# file = open("my file.txt",'a')
# file.write("python django")
# file.close()
# file = open("my file.txt",'r')
# print(file.read())
# file.close()
# with open("my file.txt",'r') as file:
#     print(file.read())
#     file.close()
# with open("my file.txt",'a') as file:
#     file.write(" duration 6 month")
#     file.close()
# with open("my file.txt",'r') as file:
#     print(file.read())
#     file.close()
# # import os  # file remove
# # os.remove("my file.txt")
#
#  #1)to check wheather a file is exixt or not (python check if file exists)
# import os
#  #os.remove("sample.txt)
#file_path =r'exam17.py'
# x=os.path.exists(file_path)
# if x:
#     print(f"{file_path} the file is existing")
# else:
#     print(f"the file{file_path} is not existing")
#
#2) python check file size
import os
y=os.path.getsize('exam17.py')
print(y)

#3) python count number of lines in a file
# filename='exam17.py'
# count_lines=0
# with open(filename,'r') as files:
#     for i in files:
#         count_lines=count_lines+1
# print()
# print(count_lines)

with open("exam17.py",'r')as fp:
    print("total lines",len(fp.readlines()))
#4) python search for a string in text files

with open('exam17.py','r')as lc:
    string=lc.read()
    #print(string)
    check_str=input("enter the string:")
    if check_str in string:
        print(check_str,'found')
    else:
        print(check_str,'not found')
    lc.close()


#5) read specific lines from a file in python
import linecache
specific_line=linecache.getline("reethu.txt",2)
print(specific_line)


# # open ths sample file used
# file=open('exam17.py')
#
# #read the content of the file opened
# # content=file.readlines()
# # # read 10 th line from the file
# # print("tenth line")
# # print(content[9])
# # #print first 3 lines of file
# # print("first 3 lines")
# # print(content[0:3])
# with open('exam17.py','r')as lc:
#      lines=lc.readlines()
#      print("no:of lines:",len(lines))
#      lines_no=int(input("enter the number;"))
#      print(lines[lines_no])
#      lc.close()
#delete lines from file in python
with open('reethu.txt','r')as ree:
    lines=ree.readlines()

with open("reethu.txt",'w') as fw:
     for number, line in enumerate(lines):
              if number not in [1,2]:


                fw.write(line)




#python to write list to file
list1=['mango','reethu']
with open("item_list.txt",'w')as ree:
    #for i in list1:
        ree.write('\n'.join(list1)) #ree.write(i+"\n")
ree.close()
# names=['rat','cat']
# with open("nuts.txt",'w')as fp:
#     fp.write('\n'.join(names))
# fp.close()
# # python 1.list files in a directory
# 2 count no of files in directory
# 3 list files in a directory with extension .txt


# import os
# list1=os.listdir(r'path')
# print("list of files:",list1)
   #or dirpath=r'path'
   #def listfil(dir_path):
   #file=os.listdir(dirpath)
   #return file
   #file_list=listfil(dir_path)
   #print(file_list)
   #for i in file_list:
   #print(i)
# count=0
# for i in list1:
#     count=count+1
# print("no:of count:",count)
# for i in list1:
#     if i.endswith(".txt"):
#         print("files with extension .txt:",i)
#
#python program to get file creation and modification date time
import os.path,time
newfile=open("sample.txt",'w')
newfile.write("hai hello")
print("created time:",time.ctime(os.path.getctime("sample.txt")))
print("last modified time:",time.ctime(os.path.getmtime("sample.txt")))
# python to remove or delete non empty folder
#import shutil
#shutil.rmtree(r'path')