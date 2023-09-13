#set is inmutable,unchageable,unordered,unindexed,not allow duplicates
set1={"reethu",12,"safna","bca","bca",12}
print(set1)
# elements asses
#by list method
set1={"reethu",12,"safna","bca","bca",12}
x=list(set1)
print(x)
print(x[0])
#values add
set1={"reethu",12,"safna","bca","bca",12}
x=set1.add("miya")
print(set1)
#remove
set1={"reethu",12,"safna","bca","bca",12}
y=set1.remove("reethu")
print(set1)
#discard
z=set1.discard("safna")
print(set1)
#pop
y=set1.pop()
print(y)
#uppdate

set1={"reethu",12,"safna","bca","bca",12}
set2={"diya"}
z=set1.update(set2)
print(set1)

#multiple datatype include in set
set1={"reethu",12,"safna","bca","bca",12}
set2=["diya"]
print(type(set2))
z=set1.update(set2)
print(set1)
print(type(set1))

######
set1={"reethu",12,"safna","bca","bca",12,(1,2,3)}
print(set1)
x={set[2,3,4]}
print(type(x))
print(x)
#union |
a={1,2,3,4,5,"priya","ka"}
b={4,5,6,7,8,"diya","ka"}

print(a.union(b))

#intersection &

print(a.intersection(b))
#difference_
print(a.difference(b))
#symmetric difference^
print(a.symmetric_difference(b))
#difference update
x=a.difference_update(b)
print(a)
#symmetric update
#y=a.symmetric_difference_update(b)
#print(a)
#intersection update
#y=a.intersection_update(b)
#print(a)


# return a set of elements present in set a or b but not both
set1={10,20,30,40,50}
set2={30,40,50,60,70}
a=set1.symmetric_difference(set2)
print(a)
#output ={20, 70, 10, 60}
#update set1 by adding items from set2 ,except common items
set1={10,20,30,40,50}
set2={30,40,50,60,70}
a=set1.symmetric_difference_update(set2)
print(set1)
#output={20, 70, 10, 60}