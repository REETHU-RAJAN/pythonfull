dict1 = {5: 2, 6: 3, 7: 4, 8: 1, 9: 0}
val = list(dict1.items())
print(val)
newval = []
#newvalf = []
for i in val:
    irev = i[::-1]
    newval.append(irev)
print(newval)
val.clear()
newval.sort()
print(newval)
for i in newval:
    irevf =  i[::-1]
    val.append(irevf)
print(val)
desending = val[::-1]
print(desending)


 #dupilcates remove in dict(remove unique value print)


listofdict = [{"v": "s001"}, {"v": "s002"}, {"vI": "s001"}, {"V1": "s005"}, {"VII": "s005"}, {"v": "s009"}]
set_ofvalue = set()
k=[]
for i in listofdict:
    for value in i.values():
        set_ofvalue.add(value)
print(set_ofvalue)
# print only unique value:


def count(arr, n):
    visited=[False for i in range(n)]
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1,n,1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        if count == 1:
            print(arr[i])
dict1={"v":"s001","v1":"s002","v2":"s001","v3":"s005","V4":"s005","v5":"s009"}
arr1=dict1.values()
arr=list(arr1)
print(arr)
n=len(arr)
count(arr,n)