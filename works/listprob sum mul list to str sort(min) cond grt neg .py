#write a python program to find the sum of all numbers in a list
#sum of all items in a list  list=[1,2,3,4,5]
my_list=[1,2,3,4,5]

#print(sum(my_list))
#by using loop method
sum=0
for i in my_list:
    sum=sum+i
print(sum)

#output = 15
#................................
#multiply all items in a given list
mul=1
for i in my_list:
    mul=mul*i
print(mul)
#............................
#convert list to string
x=["p","y","t","h","o","n"]
z=''.join(x)
print(z)
str1=""
for i in x:
    str1+=i
print(str1)
#...............................
#condition
a=13

b=11
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:print("b is less than a")
#......................................
#write a program to seperate negative and positive numbers from  a given list(accept input from user)

a=[1,7,-3,-4,8,0,-9]
x=[]
y=[]
z=[]
for i in a:
    if i>0:
        x.append(i)
    elif i==0:
       z.append(i)
    else:
        y.append(i)

print(a)
print(x)
print(y)
print(z)
#output = a=[1, 7, -3, -4, 8, 0, -9], x=[1, 7, 8], y=[-3, -4, -9], z=[0]
#....................................
#write a program to find largest number in a given list without using max()

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
