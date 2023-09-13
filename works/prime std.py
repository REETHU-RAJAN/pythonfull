def is_prime(number):
   if number<=1:
      return False
   for divisor in range(2,number):
      if number%divisor==0:# if the number is divisible by any of these divisors,return false,indicating not prime
        return False
   return True
num=int(input("enter the number:"))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

# fibonacci(0,1)

num=int(input("enter a number:"))
def fibonacci(num):
    n1, n2 = 0, 1
    for i in range(num):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
    return(" ")
print(fibonacci(num))
#fib
num=10
n1,n2=0,1

for i in range(num):
    print(n1,end=' ')
    n3=n1+n2

    n1=n2
    n2 = n3
#fac
#factorial of number
num = int(input("enter a number"))
f = 1
i = 1
while (i <= num):

    f = f * i
    i = i + 1

print("factoial of number:", f)
#3 factorial
def facn(n):
    f=1
    for i in range(1,n+1):
        f = f * i
    return f
n=int(input("enter a number"))
print(facn(n))
#1) palindrome
num=int(input("enter the number:"))
rev=0
temp=num
while num>0:
    rem=num % 10#707 % 10=7,70%10=0, 7%10=7
    rev=(rev*10) + rem# (0*10)+7=7,(7*10)+0=70,(70*10)+7=707
    num=num//10#707//10=70, 70//10=7 ,7//10=(num<0)

if temp == rev:
    print("palindrome")
else:
    print("not palindrome")
# reverse method palindrome
num=int(input("enter the number:"))
reverse = int(str(num)[::-1])
if num==reverse:
    print("palindrome")
else:
    print("not palindrome")
# palindrome
item=("reethu","amma")
palindrome=list(filter(lambda word:word==word[::-1],item))
print(palindrome)
#......................
strings=input("enter the string")
def palindrome(strings):
    s=''
    for i in strings:
        s=i+s
    #print(s)
    if s==strings:
        print("palindrome")
    else:
        print("not palindrome")
#string='amma'
palindrome(strings)
#........................
str="malayalam"
string=[str[i] for i in range(len(str)-1,-1,-1)]
x=''.join(string)
if x==str:
    print("palindrome")
else:
    print("not palindrome")
# even and odd without lambda
num = [1, 2, 4, 46, 77, 96, 4, 3]
def check_even(num):  # def even(num) for i in range (num): even_new=[]
    if num % 2 == 0:
        return True
    return False
even_num = list(filter(check_even, num))
print(even_num)
### even without true false
num = [1, 2, 4, 46, 77, 96, 4, 3]
def even(num):
    even_num = []
    for i in range (num):
        if num % 2 == 0:
           even_num.append(i)
        return even_num
print(even_num)
#even_odd
even_odd={k:('even' if k %2 ==0 else 'odd') for k in range(1,11)}

print(even_odd)
#even odd using list compression
n=[1,2,3,4,5]

even=[i*2 for i in n if i%2==0]
print(even)
odd=[j for j in n if j%2!=0]
print(odd)
# write a program to create even numbers and another list of odd numbers from a given list
a=[2,3,4,5,6,7,8,9,0,1]
x=[]
y=[]
for i in a:
    if (i % 2)==0:
        x.append(i)

    else:
        y.append(i)
print("even num:",x)
print("odd num:",y)
# output =even num: [2, 4, 6, 8, 0]
# odd num: [3, 5, 7, 9, 1]
#.................................................
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

#by using sorting method
a=[1,7,-3,-4,8,0,-9]
a.sort(reverse=True)
print(a)
print(a[:1])
#loop method
a=[1,7,-3,-4,8,0,-9]
max=a[0]
for i in a:
    if i>=max:
        max=i
print(max)
#output = 8
is_even_list=[lambda arg=x: arg*10 for x in range(1,5)]
for item in is_even_list:
    print(item())

#
max=lambda a,b : a if(a>b) else b
print(max(1,2))

n=[5,90,2,10]
sorted_n = sorted(map(str,n))
print(sorted_n)
# remove duplicates using dict
list1=["apple","banana","apple"]
list1=list(dict.fromkeys(list1))
print(list1)
#remove repeted letters from string
s2 = ["lets google the pineapple"]
print("given list:",s2)

s1="".join(s2)

print(s1)
print(type(s1))
l= " "
for i in s1:
    if i in l:

        continue
    else :
           l = l+i
          #print (l)
print("duplicates removed list:",l)
x=list(l)
print(x)
#write a program to find common number from 2 list
a=[1,2,3,4,5,6,7]
b=[9,2,3,5]
#useing set
a_set = set(a)
b_set = set(b)
0
if (a_set & b_set):
    print(a_set & b_set)
else:
    print("No common elements")
 #output = {2, 3, 5}
#by loop method
a=[1,2,3,4,5,6,7]
b=[9,2,3,5]
x=[]
for  i in a:

     if i in b:
        x.append(i)
print("common elements:",x)
#output = common elements: [2, 3, 5]
#.................................................
#write a program to remove repeated elements in given list without using built-in methods
a=["let's","google","the","pineapple","photo","google","photo"]
x=[]
for  i in a:

     if i not in x:
        x.append(i)
print("removed repeat elements:",x)