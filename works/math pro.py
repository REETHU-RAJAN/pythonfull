#taking odd valus from seq and print its square
import math
y=[]
num=[int(i)for i in input("enter the no:").split(',')]
print(num)
for i in num:
    if i%2!=0:
        y.append(i)
print("odd list:",y)
p=[]
for i in y:
    p.append(math.pow(i,2))
print(",".join(map(str,p)))