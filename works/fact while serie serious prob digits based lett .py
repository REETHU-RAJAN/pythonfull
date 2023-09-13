# 1) factorial
num = int(input("enter a number"))
f = 1
i = 1
while (i <= num):
    f = f * i
    i = i + 1

print("factoial of number:", f)
# output enter a number4
# factoial of number: 24
# ................................................

# 2)write a while loop statement to print the following series
# 105,98,97......7
num = 105
while (num >= 7):
    print(num)
    num = num - 7
    # .................................................

# 3)write a program to display the number names of the digits of a number entered by user,for example if the number is 231 then output should be two,three, one

num1= input("enter a number")
l1=list(num1)
l=len(l1)
i=0
n={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
while(i<l):
    print(n[int(l1[i])],end=' ')

    i=i+1

    # output =enter a number787
    # seven eight seven
#...........................................................
 #4) write a program to find sum of following series
#s=1+4-9+16-25.....nterms
num1 = int(input("enter a number"))
s = 0
sp = 1
sn = 0
i = 2
while (i <= num1):
    if i % 2 == 0:
        sp = sp + i ** 2
        i = i + 1
    else:
        sn = sn + i ** 2
        i = i + 1

print(sp - sn)
#5)write a program to print the following series till n terms
# 2,22,222,2222,......n terms

num1 = int(input("enter a number"))
st='2'
i=0
while(i<=num1):
    print(st,end=',')
    st=st+'2'
    i=i+1

    # output=enter a number7
    # 2,22,222,2222,22222,222222,2222222,22222222,

#6)    write a program to find sum of following series
# 1+2+6+24+120+.....n terms
num1 = int(input("enter a number"))
s=0
pr=1
i=1
while(i<=num1):
    pr=i*pr
    print(pr,end="+")
    s=s+pr
    i=i+1
print("=",s)

# output =1+2+6+24+= 33