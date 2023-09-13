# function and argument
# sum of natural numbers
num=int(input("enter the number:"))
sum=0
for i in range(num+1):
    sum=sum+i
print(sum)
# using funtion

def sum_natural(num):
    sum=0
    for i in range(num + 1):
        sum = sum + i
    return sum
print(sum_natural(num))
#greatest number
num1=123
num2=789
num3=9897
if num1>=num2 and num1>=num3:
    print("num1 great")
elif num2>=num1 and num2>=num3:
    print("num2 great")
else:
    print("num3 great")


#using funtion
def max():
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max())

# sum of numbers in list using function
num=[1,7,8,9]
def sum_list(num):
    sum=0
    for i in num:
        sum = sum + i
    return sum
print(sum_list(num))

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Reethu", "Rajan")