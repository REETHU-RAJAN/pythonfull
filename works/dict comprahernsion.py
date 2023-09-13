# dictionary comprehension
#dictionary={key:value for vars in iterable}
# square
square_dict={}
for num in range(1,11):
    square_dict[num]=num*num
print(square_dict)
# dictionary comprehension
square_dict={num:num*num for num in range(1,11)}
print(square_dict)

# prise
old_price={'milk':1.02,'cofee':2.5,'bread':2.5}
dolar_to_pound =.76
new_price={key:value * dolar_to_pound for (key,value) in old_price.items()}
print(new_price)
#zip
keys=['a','b','c','d','e']
values=[1,2,3,4,5]
mydict={k:v for (k,v) in zip(keys,values)}
print(mydict)
#even_odd
even_odd={k:('even' if k %2 ==0 else 'odd') for k in range(1,11)}

print(even_odd)
#value eve
first_dict={'jack':38,'jin':40,'ree':35}
#eve_dict={k:v%2==0 for (k,v) in first_dict.items()}
eve_dict={k:v for (k,v) in first_dict.items() if v%2==0}
print(eve_dict)
#enumerate type
keys=['a','f','c','d','e','f']
enu={keys[i]:keys[i+1] for i in range(0,len(keys),2)}
print(enu)
fistval=[]
for i in range (0,len(keys),2):
    fistval.append(keys[i])
secval=[keys[j]for j in range (1,len(keys),2)]
print(dict(zip(fistval,secval)))
# if else dict
orginal_dict={'jack':38,'mic':48}
new={k:('old' if v>40 else 'young') for (k,v) in orginal_dict.items()}
print(new)
# array
dict={
    k1:{k2:k1 * k2 for k2 in range(1,6)} for k1 in range(2,5)
}
print(dict)
# example 2 condition
first_dict={'jack':38,'jin':33,'ree':55}
new_dictt={k:v for (k,v) in first_dict.items() if v % 2!=0 if v<40}
print(new_dictt)
