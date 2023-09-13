#5)write a funtion that given a list of non negative integers,arranges them such that they form the largest possible number. ex:given[50,2,1,9],the largest formed number is 95021
from _functools import cmp_to_key
n=[50,6,9,75]

def get_key(first,second):
    if str(first)+str(second)>str(second)+str(first):
        return -1
    return 1
result=sorted(n,key=cmp_to_key(get_key))
result="".join(str(integer)for integer in result)
print(int(result))