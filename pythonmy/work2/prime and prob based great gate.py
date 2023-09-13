# 1) to check wheather a number prime or not
num = int(input("enter the number"))
flag = 0
for i in range (2,num):
     if num % i == 0:
          flag = 1
          break
if flag == 1 :
   print("the num is not prime",end='')
else :
     print("the num is prime",end='')
     # num = int(input("enter the number"))
     # if num<1:
     # for i in range(2, num):
     #     if num % i == 0:
     #          print("the num is not prime", end='')
     #         break
     #      else:
           # print(num,"is prime")
     #
     # else:
     #     print("the num is not prime", end='')


#............................................

#2)write a program to find those numbers divisible by 7 and multiple of 5
num =int(input("enter the number"))
if num % 7==0 and num % 5==0:
     print("number divisible by 7 and multiple of 5")
else:
     print("number not divisible by 7 and multiple of 5")

#........................................................
#3) to find a person vote or not
num =int(input("enter the age"))
if num >=18:
     print("the person can vote")
else:
     print("the person can't vote")

    #......................................................

 # 4) write a program to give bonus of 5% to employee if he/she year of service is more than 5 years . ask user to their salery and service and print the net bonus amount

salery= int(input("enter the salery"))
service =int(input("enter the service"))
if service >=5:
     salery=salery+5%(salery)
     print ("bonus =",salery)
else:
     print("not eligible for get bonus")
#......................................................
 # 5) write a program traffic light if light is green then car is allow to go, yellow then wait and if red then stop
light=input("enter the colour:")
if light =="green":
       print("allow to go")
elif light== "yellow":
    print("car should wait")
elif light=="red":
    print("car should stop")
else:
    print("invalid colour")
#6) a school has following rules for grading system:
#a.below 25-f, 25 to45-e,45 to 50-d, 50 to 60 c, 60 to 80 b, above 80 a
mark=int(input("enter the mark"))
if (mark < 25) :
     print("fail")
elif (mark>=25 and mark < 45) :
        print("grade e")
elif (mark >= 45 and mark < 50):
        print("grade d")
elif (mark >= 50 and mark < 60):
        print("grade c")
elif (mark >= 60 and mark < 80):
       print("grade b")
elif (mark >=80):
      print("grade a")
else:
    print("no grade")
   # 7)  take three int values from user and print greater value
n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number:"))
n3 = int(input("enter the third number:"))
if (n1 >= n2) and (n1 >= n3):
    largest = n1
elif (n2 >= n1) and (n2 >= n3):
    largest = n2
else:
    largest = n3
    print("the largest number is:", largest)
