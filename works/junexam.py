#1.to create fibonocci serious with python fn
#2 number is palindrome or not
 # 1fibonacci anwer
num=int(input("enter a number:"))
def fib(num):
    n1,n2=0,1
    for i in range(num):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3
    return " "
print(fib(num))
#2 palindrome answer
n=int(input("enter a number"))
x=int(str(n)[::-1])
if x==n:
    print("num is palindrome")
else:
    print(" num is not palindrome")
#3 print inverted pyrimid pattern
n=int(input("enter a number"))
for i in range (n,0,-1):
    for j in range (n-i):
        print(" ",end=" ")
    for k in range (2*i-1):
        print(" *",end="")
    print()
n=int(input("enter a number"))
for i in range (n+1):
    for j in range (n-i):
        print(" ",end=" ")
    for k in range (2*(i)-1):
        print(" *",end="")
    print()
#4 calculate the area of a triangle using function
def area(a,b):
   #a=float(input("enter one side length"))
    #b=float(input("enter 2nd side length"))
    x=.5*a*b
    print(x)
area(4,2)
#tri
l=float(input("enter one side length"))
b=float(input("enter 2nd side length"))
def tri(x,y):
    area=(x*y)/2
    print(f'area of tri:{area}')
tri(l,b)
#5 how do i get last elememrt of a list in python
listitems=["apple","orange","banana",67,90]
print(listitems[-1:])
