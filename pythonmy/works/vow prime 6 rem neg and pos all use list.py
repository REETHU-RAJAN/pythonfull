#lift comprehensive
# list comprehensive vowels remove
num=input("enter the string")
print(num)
n=list(num)
print(n)
nonvow=[i for i in n if i not in 'AEIOUaeiou']
print(nonvow)
k=''.join(nonvow)
print(k)
#prime numbers
list1=[1,2,3,4,5,6,7,8,9,11,21]

#prime1=[i for i in list1 if 0 not in[i%j for j in range(2,i)]]
prime2=[i for i in list1 if all(i%j != 0  for j in range(2,i))]

#print(prime1)
print(prime2)
#find all of the numberx in given list that have 6 in them
nums=[65,87,66,97]
n6=[num for num in nums if '6' in str(num)]
print(n6)
# find postive and negative number in list
num=[-1,-3,2,4,5,0]
pos=[i for i in num if i>0]
print(pos)
neg=[i for i in num if i<0]
print(neg)