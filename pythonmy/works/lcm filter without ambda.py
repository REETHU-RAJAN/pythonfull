#FILTER() WITHOUT USING LAMBDA
def char(s):
    return s[0]=="a"
fruit=["apple","banana","kiwi"]
filter_fruit=filter(char,fruit)
print(list(filter_fruit))
# lcm
def calculate_lcm(x,y):
    if x>y:
        greater= x
    else:
        greater = y
    while (True):
        if((greater % x==0) and (greater % y ==0)):
            lcm = greater
            break
        greater +=1
    return lcm
num1 = int(input("enter the first num:"))
num2 = int(input("enter the second num:"))
print(calculate_lcm(num1,num2))
def add(a,b=5,c=1):
    return (a+b+c)
print(add(3))
#Output:9
print (add(b=10,c=15,a=20))
#Output:45
#2. During a function call, only giving mandatory argument as a keyword argument. Optional default arguments are skipped.
print (add(a=1))
#Output:7

