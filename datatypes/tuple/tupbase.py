#tuple inmutable indexed allow dupilcates and ordered
thistuple=("apple", 99 ,"pp","apple")
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
print(thistuple[1:])
print(thistuple[::-1])
print(thistuple[::-2])
print(thistuple[:-1])
print(thistuple[:1])
print(len(thistuple))
#add
y=list(thistuple)
y[0]='grass'
print(tuple(y))
#type ,
z=('orange',)
print (type(z))
#concagtion
thistuple+=z
print(thistuple)
#multiple acces list and tuple
z=("apple","op", 99 ,["bb","aaa",44],"pp","apple")
print(z)
print(z[2])
#remove
y=list(z)
print(y)
y.remove("apple")
print(y)
y.pop(-1)
print(y)
#reverse

y=list(z)

y.reverse()
print(y)
#reverse only list


y=list(z)
p=y[3][::-1]

print(p)
#check wheather an element exist within a tuple
tuple1=("apple",[10,20,30],(5,12,25),1,5,6,7)

print("apple" in tuple1)

print("bab" in tuple1)
#covert tuple into string
tuple2=("s","t","r","i","n","g")

y=''.join(tuple2)
print(y)
#count the number of occurance of item 50 from a tuple
tuple1  = (20,50,70,50,60)
z=tuple1.count(50)
print(z)
#enumurate
tuple2=("s","t","r","i","n","g")
y=enumerate(tuple2)
y=list(y)
print(y)
#use tuple
z=tuple(y)
print(z)
#all true and postive
tuples=("true","false")
print(all(tuples))

print(any(tuples))

