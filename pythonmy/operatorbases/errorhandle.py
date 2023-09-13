# error handling mechanism
# try
# except
# finally
# try:
#   doubtfulcode
# except:
# handling code
# finally:
# clean up or mandatory

# f=open("demo.txt","r")#if file not found then error
# for line in f:
#       print(line)
# print("database commit1")
# print("data base commit 2")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
try:

     res=num1/num2
     print("result",res)
except Exception as e:
    print(e.args)# shows what was the error occured before
    # print("exception occured")

print("line1")
print("line2")