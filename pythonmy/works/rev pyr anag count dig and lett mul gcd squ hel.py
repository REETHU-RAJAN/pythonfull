#1) write  a code to reverse a number


num=int(input("enter the number:"))

#temp=num
while num>0:
    rem=num % 10#707 % 10=7,70%10=0, 7%10=7

    num=num//10#707//10=70, 70//10=7 ,7//10=(num<0)

    print(rem,end='')

    #output= enter the number:978
#8 7 9
#
    #...............................
 # 2) write code of greatest common divisor
import math
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
print(math.gcd(n1,n2))

gcd = 1
for i in range(1, min(n1, n2)):
    if (n1 % 1 == 0) and (n2 % i == 0):
        gcd = i
print(gcd)

#a=int(input("enter first number"))
#b=int(input("enter second number"))
#while b:
    #a,b=b,a%b
#print(a)
#output =enter first number40
#enter second number15
#5
#...........................................

# 3)write a code to check if 2 strings are anagram or not
str1=str(input("enter the string1"))
str2=str(input("enter the string2"))
stra=sorted(str1.lower())
strb=sorted(str2.lower())
if(stra==strb):
    print("strings are anagram")
else:
    print("strings are not anagram")
    # output =enter the string1:flow
    # enter the string2:wolf
    # strings are anagram
    #............................................

#4) multipilcation table
num=int(input("enter a number"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)

    #..................................
#5)  square of 10 numbers

num=int(input("enter a number"))
for i in range(1,11):
    print(i,'*',i,'=',i*i)
    #............................................

#.................................
#7)write a program to display "hello" if a number entered by user age is a multiple of 5,otherwise print"bye"
num =int(input("enter your age"))
if num%5==0:
    print("hello")
else:
    print("bye")
#..............................................................

#9)write a program to print of half pyramid of stars
for i in range (5):
    for j in range(i+1):
        print("*",end='')
    print()
#10)count total number of digits in a number
num =int(input("enter a number"))
num_str=str(num)
count=0
for i in num_str:
    count=count+1
print(count)

# in case words
num =input("enter a word")
count=0
for i in num:
    count=count+1
print(count)