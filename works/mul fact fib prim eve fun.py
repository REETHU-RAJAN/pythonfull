#1)multiply
def mul(a,b,c):
    return (a*b*c)

print (mul(2,3,4))
#2 muliply list
def mul_num(nums):
    mul=1
    for i in (nums):
        mul = mul * i
    return mul
nums= [2,3,4]
print(mul_num(nums))
#3 factorial
def fa_n(n):
    f=1
    for i in range(1,n+1):
        f = f * i
    return f
n=int(input("enter a number"))
print(fa_n(n))

#4 print 4 to 28 even numbers using function
even=[]
for i in range(4,31):

    if i % 2 == 0:
        even.append(i)
print(even)
#list
even=[i for i in range(4,31) if i %2==0]
print(even)
#5 check wheather enter number is prime
def prime_num(a):
    flag =False
    for i in range (2,a):
        if a%i==0:
            flag = True
    if flag == True:
        print("it is not a prime")
    else:
        print("prime number")
num=int(input("enter a number:"))
prime_num(num)


#6 fibonacci series
# def fibonacci(n1,n2):
#     for i in range(1,11):
#         print(n1)
#         n3=n1+n2
#         n1=n2
#         n2=n3
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

