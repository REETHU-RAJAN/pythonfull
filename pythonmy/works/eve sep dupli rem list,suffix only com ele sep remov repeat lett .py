# write a program to create even numbers and another list of odd numbers from a given list
a=[2,3,4,5,6,7,8,9,0,1]
x=[]
y=[]
for i in a:
    if (i % 2)==0:
        x.append(i)

    else:
        y.append(i)
print("even num:",x)
print("odd num:",y)
# output =even num: [2, 4, 6, 8, 0]
# odd num: [3, 5, 7, 9, 1]
#.................................................
# write a program to print even numbers from a given list
a=[2,3,4,5,6,7,8,9,0,1]
x=[]

for i in a:
    if (i % 2)==0:
        x.append(i)
print("even only:",x)
#output = even only: [2, 4, 6, 8, 0]
#.................................................
#write a program to find common number from 2 list
a=[1,2,3,4,5,6,7]
b=[9,2,3,5]
#useing set
a_set = set(a)
b_set = set(b)
0
if (a_set & b_set):
    print(a_set & b_set)
else:
    print("No common elements")
 #output = {2, 3, 5}
#by loop method
a=[1,2,3,4,5,6,7]
b=[9,2,3,5]
x=[]
for  i in a:

     if i in b:
        x.append(i)
print("common elements:",x)
#output = common elements: [2, 3, 5]
#.................................................
#write a program to remove repeated elements in given list without using built-in methods
a=["let's","google","the","pineapple","photo","google","photo"]
x=[]
for  i in a:

     if i not in x:
        x.append(i)
print("removed repeat elements:",x)
#output = removed repeat elements: ["let's", 'google', 'the', 'pineapple', 'photo']
#.............................................
# write a program to print website suffixes (com,org,net,in) from the list
x=['www.zframez.com','www.wikipedia.org','www.asp.net','www.abcd.in']
k=x[0][-3:]
l=x[1][-3:]
m=x[2][-3:]
n=x[3][-2:]
h=(k,l,m,n)
print("suffix part:",h)
#output = suffix part: ('com', 'org', 'net', 'in')
#by using loop method
x=['www.zframez.com','www.wikipedia.org','www.asp.net','www.abcd.in']
for i in x:
    s=i.split(".")[-1]
    print(s)
#output = com ,org ,net ,in
#..............................................
#remove repeted letters from string
s2 = ["lets google the pineapple"]
print("given list:",s2)

s1="".join(s2)

print(s1)
print(type(s1))
l= " "
for i in s1:
    if i in l:

        continue
    else :
           l = l+i
          #print (l)
print("duplicates removed list:",l)
x=list(l)
print(x)