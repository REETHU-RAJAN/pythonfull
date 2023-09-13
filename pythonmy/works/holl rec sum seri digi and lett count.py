#1) python program that accepts a string and calculates the number of digits and letters
userinputt= input("enter a string seq")
digits=0
letters=0
for i in userinputt:
     if i.isdigit()==True:
          digits=digits+1
     elif i.isalpha()==True:
          letters=letters+1
print("the input string",userinputt,"has",letters,"letters and:",digits,"digits")
# OUTPUT=enter a string seqREETHU12345
# the input string REETHU12345 has 6 letters and: 5 digits

#2)write a program to find the sum of following series

#1+8+27+.....
num = int(input("enter any number:"))
s=0
i=1
while (i<=num):
    s=s+i**3
    i=i+1
print(s)
#output=enter any number:4
100

# 3) write a python program to get the following output
# 1--49
# 2--48
# 3--47
# ..
# ..
# 49--1
i = 1
j = 49
while (i <= 49 and j >= 1):
    print(i, "--", j)
    i = i + 1
    j = j - 1

# hollow rect
n=int(input("enter a number:"))
for i in range(n):
    for j in range (n):
        if i==0 or j==0 or j==n-1 or i==n-1:
           print("* ",end="")
        else:
           print(" ",end=" ")
    print()
    #output=enter a number:5
#* * * * *
#*       *
#*       *
#*       *
#* * * * *





