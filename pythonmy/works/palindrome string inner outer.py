
# palindrome
item=("reethu","amma")
palindrome=list(filter(lambda word:word==word[::-1],item))
print(palindrome)
#......................
strings=input("enter the string")
def palindrome(strings):
    s=''
    for i in strings:
        s=i+s
    #print(s)
    if s==strings:
        print("palindrome")
    else:
        print("not palindrome")
#string='amma'
palindrome(strings)
#........................
str="malayalam"
string=[str[i] for i in range(len(str)-1,-1,-1)]
x=''.join(string)
if x==str:
    print("palindrome")
else:
    print("not palindrome")
# inner  nexted fn
def create_adder(x):
    def adder(y,z):
        return x+y+z
    return adder
add = create_adder(15)
print(add(10,2))
#print(create_adder(15)(10,2))
#..................
def num_1(a):
    def num_2(b):
        return a*b
    return num_2
print(num_1(3)(2))
