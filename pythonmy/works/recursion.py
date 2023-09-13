#recursion
#sum of 10 numbers
def counter(c):
    if c<=0:
        #print(c)
        return c
    else:
        return c+counter(c-1)
print(counter(10))
   # y= c+counter(c-1) 10+9+..........+0
   #print(y)
   #return y
 # or sum method
def tri_recursion(k):
    if(k>0):
        result=k + tri_recursion(k-1)
        print(result)
        return result
    else:
        result = 0
        print(result)
    return result
print(tri_recursion(6))
# factorial
def fact(n):
    if n==1:
    #print(n)
         return 1
    else:
      x=n*fact(n-1) # 2*1=2, 3*2!,.....5*4!=120
      print(x)
      return x
print(fact(5))
#fibonacci serious
def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(7))

# # sum of digits
# def sum_digits(n):
#     if n==0:
#        return 0
#
#     else:
#
#         digit = n % 10  # 153 %10=3,15%10=5,1%10=1
#         sum = digit + sum_digits(n//10) # 0+27=27,27+(5*5*5)=152,152+(1*1*1)=153
#
#         return sum
# result=sum_digits(34)
# print(result)

#power
def number_pow(n,x):
    if x==0:
        return 1
    else:
        y=n*number_pow(n,x-1)
        return y
print("power:",number_pow(2,4))
#palindrome
n=int(input("enter a num :"))
def pali(n):
    def reverse(n,rev=0):
        if  n==0:
            return rev
        else:
            a=((rev*10)+(n%10))
            rev=reverse(n//10,a)

            return rev
    if reverse(n)==n:
        print("pali")
    else:
        print("not pali")
print(pali(n))
def tri_recursion(k):
    if(k>0):
        return k + tri_recursion(k-1)
    else:
        result = 0
        #print(result)
    return result
print(tri_recursion(6))
#palindrome
s=input("enter the string:")
def pali(s):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return pali(s[1:-1]) # exclude first and last data
        else:
            return False
print(pali(s))
# sum of digits
n=1330
def sum_of_dig(n):
    if n<=0: # n<10
        return n
    else:
        return n%10+sum_of_dig(n//10)
print(sum_of_dig(n))
#product of digits
n=133
def pro_of_dig(n):
    if n<=1: # n<10
        return n
    else:
        return n%10*pro_of_dig(n//10)
print(pro_of_dig(n))