#1)leap year
year=int(input("eneter a year"))
if((year % 4==0) and (year % 100!=0) or (year % 400==0)):
    print("its leap year")
else:
    print("not leap year")
#2 while loop print 1 to 10
print("print 1 to 10")
i=1
while i<=10:
    print(i)
    i+=1
#3)while loop print 10 to 1
print("print 10 to 1")
i=10
while i>=1:
    print(i)
    i-=1
#4)sum of natural numbers
num=int(input("enter a num"))
sum=0
i=1
while i<=num:


    sum = sum+i
    i += 1
    print(sum)
print(sum)
# using if range
num1 =int(input("enter number of natural num"))
sum=0
for i in range(1,num1):

    sum = sum+i
    print(sum)
print(sum)