#duplicates remove in list
list1=['apple','banana','apple']
list1=list(dict.fromkeys(list1))
print(list1)

#even odd using list compression
n=[1,2,3,4,5]

even=[i*2 for i in n if i%2==0]
print(even)
odd=[j for j in n if j%2!=0]
print(odd)

# fruts a
fruits=['apple','banana','grapes','kiwi','orange']
fuia=[i for i in fruits if 'a' in i]
print(fuia)
fuin=[i for i in fruits if 'a' not in i]
print(fuin)

#reverse
num=int(input("enter the number:"))

rev=''
while num>0:
    rem=num % 10#707 % 10=7,70%10=0, 7%10=7
    rev=rev+str(rem)
    num=num//10#707//10=70, 70//10=7 ,7//10=(num<0)

print(rev,end='')