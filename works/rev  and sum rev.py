l1=[2,4,3]
l2=[5,6,4]
l1.reverse()
l2.reverse()
x=[]
for i in l1:
    x.append(str(i))
print(x,end='')
print('\n')
y=[]
for i in l2:
    y.append(str(i))
print(y,end='')
print('\n')
num1=0
num2=0
for i in x:
    num1=(num1*10)+(ord(i)-48)
print(num1)
for i in y:
    num2=(num2*10)+(ord(i)-48)
print(num2)
a=num1+num2
rev=0
num=a
while (num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("result rev=",rev)
