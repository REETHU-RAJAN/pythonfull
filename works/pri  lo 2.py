# print your name inside love pattern
num=int(input("enter the colomn number"))
msg=input("enter a message")
l=len(msg)
n=int(num//2)
for i in range(n):
    print(' '*(n-i-1) + '* '*(i+1), end='')
    if num %2==0:
        for j in range(2*(n - i - 1)):
            print(' ', end='')
    else:
        for j in range(2 * (n - i - 1)+1):
             print(' ', end='')
    for j in range(i + 1):
        print('* ', end='')
    print()
if num%2 ==0:
    if l%2==0:
        print("* " * ((num - l)//2) + " ".join(msg) + " *" * ((num - l)//2))# both even
    else:
        print("* " * ((num - l)//2) + " ".join(msg) + " *" * (((num - l)//2)+1)) #col even and msg odd
else:
    if l%2==0:
        print("* " * ((num - l)//2) + " ".join(msg) + " *" * (((num - l)//2)+1)) # col odd and msg even
    else:
        print("* " * ((num - l)//2) + " ".join(msg) + " *" * ((num - l)//2)) # both odd
for i in range (num,0,-1):
     print(' '*(num-i) + '* '*(i))
# output=enter the colomn number10
# enter a messageREETHU
#     *         *
#    * *       * *
#   * * *     * * *
#  * * * *   * * * *
# * * * * * * * * * *
# * * R E E T H U * *
# * * * * * * * * * *
#  * * * * * * * * *
#   * * * * * * * *
#    * * * * * * *
#     * * * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *

#print this pattern

string = input("enter an string:")
leng = len(string)
for row in range(leng):

    for col in range(row+1):
        print(string[col],end='')

    print()
# output=    enter an string:python
# p
# py
# pyt
# pyth
# pytho
# python

#pascals triangle
n=int(input("enter the row num:"))
list1= []
for i in range (n):
    temp_list=[]
    for j in range (i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(temp_list)
for i in range(n):

    for j in range(n-i-1):
        print(format(" ","<2"), end='')
    for j in range (i+1):
        print(format(list1[i][j],"<3"), end=' ')

    print()
# output=    enter the row num:7
#             1
#           1   1
#         1   2   1
#       1   3   3   1
#     1   4   6   4   1
#   1   5   10  10  5   1
# 1   6   15  20  15  6   1

# love
for row in range (6):
    for col in range (7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col)==2 or ((row+col)==8):
            print('*',end='')
        else:
            print(end=' ')
    print()
# output=
#  ** **
# *  *  *
# *     *
#  *   *
#   * *
#    *

# hollow inside rectangle pattern

n = int(input("enter the no of rows:"))

for i in range(n,0,-1):
    for j in range(i,0,-1):
         print('*', end=' ')
    for j in range(2*(n-i)):
         print(' ', end=' ')
    for j in range(i, 0, -1):
         print('*', end=' ')

    print()

for i in range(i,n):
     for j in range(i+1):
         print('*', end=' ')
     for j in range (2*(n -i-1)):
        print(' ', end=' ')
     for j in range(i+1):
         print('*', end=' ')

     print()
 # output=enter the no of rows:5
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *


n = int(input("enter the no of rows:"))

for i in range(1,n+1):
    #step1:
    for j in range(1,n+1):
         print(n-min(i,j)+1, end=' ')
    #step2
    for j in range(n-1,0,-1):
         print(n-min(i,j)+1, end=' ')
    print(" ")
    #step3
for i in range (n-1,0,-1):
        # step1:
    for j in range(1, n + 1):
        print(n - min(i, j) + 1, end=' ')
        # step2
    for j in range(n - 1, 0, -1):
        print(n - min(i, j) + 1, end=' ')
    print(" ")
 # output=enter the no of rows:4
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

