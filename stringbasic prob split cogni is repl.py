str1 = "hello world"
#string indexing
print(str1[0])
print(str1[4])
print(str1[8])
print(str1[5])
print(str1[-1])
print(str1[-3])
#string slicing
print(str1[-4:])

print(str1[6:])
print(str1[:4])
print(str1[1:5])
print(str1[:-1])
print(str1[:1:-6])
print(str1[-3:])
print(str1[-5:])
print(str1[1:-7])
print(str1[1:-6])
print(str1[::-1])
print(str1[:5:-1])
print(str1[:5])
print(str1[5::-1])
print(str1[6::-1])
print(str1[5:])
print(str1[1::-1])
print(str1[::-2])
print(str1[:-2])
print(str1[-2:])

str2 = "reethurajan"
print(str2[:6])
print(str2[6:])
print(str2[::-1])
print(str2[5::-1])
print(str2[:5:-1])
print(str2[::-2])
print(str2[:])
print(str2[::])
print(str2[::1])
str1 = "hello world"
#string funtions
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.find("world"))
list1 = ["apple","orange"]
print(type(list1))
x = "#".join(list1)
y = "-".join(list1)
z = " ".join(list1)
k=x+y+z
print(k)
print(type(k))

name = "shiva 11"
print(type(name))
print(name.split())
print(type(name))
#iscase
x = name.isupper()
print(x)
x = name.isnumeric()
print(x)
x = name.isalpha()
print(x)
x = name.islower()
print(x)
print(len(name))

x = name.isspace()
print(x)
#conganate problem
str1 = "python"
str2 = "luminar"
mid = int(len(str1)/2)
print(mid)
x = str1[:mid]
print(x)
x =x+str2
print(x)
y=str1[mid:]
print(y)
x =x+y
print(x)
# first,middle and last  chara conganate
s1 = "python"
s2 = "luminar"
mid1 = s1[int(len(s1)/2)]
print(mid1)
mid2 = s2[int(len(s2)/2)]
print(mid2)
x = s1[:1]
print(x)
y = s2[:1]
print(y)

a = s1[-1:]
print(a)
b = s2[-1:]
print(b)
k=x+y+mid1+mid2+a+b
print(k)
#replacemet and congation
s1 = "i like apples"
s2 = " how are you"
x = s1.replace("apples","grape")
print(x)
print( x + s2)
print(list(s1))
z = ''.join(s1)
print(z)
print(tuple(s1))
print(set(s1))



