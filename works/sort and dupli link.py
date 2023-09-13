# Question:1
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# n=input("enter the seq")
# list=n.split(",")
# sorted_n = sorted(map(str,list))
# print(str(sorted_n))
# print("".join(str(sorted_n)))

items=["without","hello","bag","world"]
items.sort()
print(",".join(items))
# Question:2
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


w=[str(i) for i in input("enter words:").split(" ")]
x=[]
for i in w:
    if i not in x:
        x.append(i)
x.sort()
z=' '.join(x)
print(z)






# Question:5
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



n=int(input("enter the range"))
d={i:i*i for i in range (1,n+1)}
print(d)

n=int(input("enter the range"))
d={}
for i in range (1,n+1):
    d[i]=i*i
print(d)

n=int(input("enter the range"))
d={}
for i in range (1,n+1):
    d.setdefault(i,i*i)
print(d)
# QUESTION 6
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

n=input("enter the number")
list=n.split(",")
tuple=tuple(list)
print("list:",list)
print("tuple:",tuple)

l=[int(i) for i in input("enter the number:").split(",")]
print(l)









