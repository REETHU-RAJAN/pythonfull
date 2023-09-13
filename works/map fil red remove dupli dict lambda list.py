#print 0 to 4
neww=[x for x in range(10) if x<5]
print(neww)
# remove duplicates using dict
list1=["apple","banana","apple"]
list1=list(dict.fromkeys(list1))
print(list1)
#matrix [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
matrixx=[[i for i in range(5)] for i in range(4)]
print(matrixx)


# BUILD IN FN MAP,FILTER,REDUCE (fn,iterable)
from functools import reduce

num1 = [1, 3, 5]
num2 = [2, 4, 6]
res = map(lambda x, y: x * y, num1, num2)
print(list(res))
num = [1, 5, 6]
srq = []
for i in num:
    srq.append(i ** 2)
print(srq)
srr = [i ** 2 for i in num]
print(srr)
# MAP
srrs = list(map(lambda x: x ** 2, num))
print(srrs)
# FILTER
num = [-2, -3, 4]
fil = list(filter(lambda x: x < 0, num))
print(fil)
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

# reduce
# product here x=first ip y=2nd ip after first iteration product save in x and next value in y
list1 = [1, 5, 4]
produt = reduce((lambda x, y: x * y), list1)
print(produt)
# sum of numbers
num = int(input("enter the number:"))
sum = reduce((lambda x, y: x + y), range(num + 1))
print(sum)
# vowels present check without lambda
lett = ['a', 'g', 'h', 'i', 'e']
def filter_vow(lett):
    vow = ['a', 'e', 'i', 'o', 'u']
    return True if lett in vow else False
filtered = list(filter(filter_vow, lett))
print(filtered)
