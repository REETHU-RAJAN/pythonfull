#lambda funtion
str1="reethu is a student"
rev_upper=lambda string: string.upper()[::-1]
print(rev_upper(str1))
#
is_even_list=[lambda arg=x: arg*10 for x in range(1,5)]
for item in is_even_list:
    print(item())

#
max=lambda a,b : a if(a>b) else b
print(max(1,2))

n=[5,90,2,10]
sorted_n = sorted(map(str,n))
print(sorted_n)