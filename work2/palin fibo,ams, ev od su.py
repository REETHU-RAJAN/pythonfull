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

#)fibanocci serous
num=10
n1,n2=0,1

for i in range(num):
    print(n1,end=' ')
    n3=n1+n2

    n1=n2
    n2 = n3

    # output 0 1 1 2 3 5 8 13 21 34
#...................................
# armstrong number

# 153=1*1*1+5*5*5+3*3*3=153
number=int(input("enter the number:"))
sum=0
temp=number
while temp>0:
    n=temp%10 # 153 %10=3,15%10=5,1%10=1
    sum =sum +(n*n*n)# 0+27=27,27+(5*5*5)=152,152+(1*1*1)=153
    temp=temp//10 # 153//10=15,15//10=1
if number==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")


#......................
# write a program to print sum of even numbers and odd numbers
a =[3,6,7,5,11,8]
esum=0
osum=0
for i in a:
    if (i % 2)==0:
        esum=esum+i


    else:
        osum=osum+i
print("sum of even num =",esum)
print("sum of odd num =",osum)
