#list
#ordered,mutable,indexing,allow dupilcate (changeable)
list_items = ["apple","banana","orange"]
list_items[0]="ab"
print(list_items)
print(list_items)
print(list_items[2])
print(list_items[-1])
print(list_items[:-1])
print(list_items[:-2])
print(list_items[::-1])
print(list_items[::-2])
print(list_items[-1:])
print(list_items[-2:])
print(list_items[-1::])
print(list_items[-2::])
print(list_items[1:])
print(list_items[0][-1])
print(list_items[0][:-1])
x = ' '.join(list_items)
print(x)
list_items[1] = "pineapple"
print(list_items)
s1 = "hi dears"
x = list(s1)
print(x)
x[1]="v"
print(x)
print(''.join(x))

list_items = ["apple","banana","orange",["python","java","react"]]
print(list_items[3])
print(list_items[3][0])
print(list_items[3][0][0])
list_items[3][1]= "angular"
print(list_items)
#append
list_items.append('vue')
print(list_items)
#insert
list_items[3].insert(1,'golang')
print(list_items)
#remove
list_items.remove('apple')
print(list_items)
list_items.remove(list_items[0])
print(list_items)


#pop for deletion
list_items.pop(0)
print(list_items)

k=list_items.pop()
print(k)
print(list_items)



#list_items.clear()
#print(list_items)
#del list_items
#print(list_items)
#reverse
list_items.reverse()
print(list_items)
list_items[1].reverse()
print(list_items)

#count
y=list_items.count("banana")
print(y)
#extend
s2=["go","seep"]
list_items.extend(s2)
print(list_items)
#sort
list_so=["appu","ammu","car"]
list_so.sort()
print(list_so)
list_so.sort(reverse=True)
print(list_so)
list_items = ["apple","banana","orange",["python","java","react"]]

list_items[3].sort()
print(list_items)

