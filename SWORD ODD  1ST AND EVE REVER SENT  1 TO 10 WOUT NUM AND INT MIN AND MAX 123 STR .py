
#1) let all odd numbers come before even numbers, and sort the odd numbers in ascending order and even numbers in descending order.eg: "1982376455" becomes'1355798642

s='123457880875'
even=[]
odd=[]
x=list(s)
#print(x)
for i in x:
    if int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)

odd.sort()

even.sort(reverse=True)
odd.extend(even)
#print(a)
b=''.join(odd)
print(b)
#output=['1', '3', '5', '5', '7', '7', '8', '8', '8', '4', '2', '0']
#135577888420


# 2)given a sentence ,reverse each word but dont reverse the sentence
str1=input("enter a sequence:")
k=str1.split(" ")
#print(k)
z=[]
for i in k:
    z.append(i[::-1])
    new=" ".join(z)
print(new)
# output=enter a sequence:my name is reethu
# ['my', 'name', 'is', 'reethu']
# ym eman si uhteer



# 3)given a sentence ,reverse  the sentence
str1=input("enter a sequence:")
k=str1.split(" ")
z=k[::-1]
new=" ".join(z)
print(new)
# output=enter a sequence:my name is reethu
# reethu is name my
#4)print number 1 to 100 without using any numbers or integers
num=ord("B")-ord("A")
for i in range(num,ord("e")):
    print(i)


#  reverse a element
num=4570
print(str(num)[::-1])


#5)convert the string '123' into 123 without using built apl int()?
n=input("enter a sequence")
#n='123'
num=0
#l=len(n)
for i in n:
    num=(num*10)+(ord(i)-48) #0*10+(49-48)=1,1*10+(50-48)=12,12*10+(51-48)=123
print(num)
#output=enter a sequence123
#123

#5) find the minimum and maximum numbers in an list in a single loop
num=[72,33,88,89]

num.sort()
print("minimum:",num[:1])
print("maximum:",num[-1:])

# n people are stand in a circle and the first person has a sword and he kills the 2nd person and gives the sword to 3rd person and soon till 99th person kill the 100th person gives the sword back to 1st person this goes until one survive.print the survivor?
person=100
a=[0]*person
for i in range(person):
    a[i]=i+1
pos=0
while (len(a)>1):
    pos+=1
    pos%=len(a)
    del a[pos]
print(a[0])


