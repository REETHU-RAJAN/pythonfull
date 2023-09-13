#1) try to create diamond pattern
n=int(input("enter a number"))
for i in range (n+1):# rows
    for j in range(n-i):#spacing
        print(' ',end=' ')
    for k in range (i):#no of * print
        print('*  ',end=' ')
    print()
for i in range(1,n):  # rows
    for j in range(i):  # spacing
        print(' ', end=' ')
    for k in range(n - i):  # no of * print
        print('* ', end='  ')
    print()
#output=
#      *
#    *   *
#  *   *   *
#*   *   *   *
#  *   *   *
#    *   *
#      *

#.........................
#2) half pyramid pattern with number
n = int(input("enter a number"))

for i in range(n + 1):  # rows
    for k in range(1,i+1):  # no of * print
        print(k, end='   ')

    print()
#0utput=4
#1
#1   2
#1   2   3
#1   2   3   4
#1   2   3   4   5




# 3) try to create hollow diamond pattern
n=int(input("enter a number"))


for i in range (n+1):# rows
    for j in range(n-i+1):#spacing
        print(' ',end=' ')
    for k in range (1,2*i):#no of * print
        if k==1 or k==2*i-1:#k==1 for left or k==2*i-1 for right
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n+1,0,-1):  # rows
    for j in range(1,n-i+2):  # spacing
        print(' ', end=' ')
    for k in range(1,2*i):  # no of * print
        if k==1 or k==2*i-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# output:
#           *
#         *   *
#       *       *
#     *           *
#   *               *
# *                   *
#   *               *
#     *           *
#       *       *
#         *   *
#           *

#4)reverse pattern from 10 to 1
n = int(input("enter a number"))
for i in range(n,0,-1):  # rows
    print(i,end=' ')
    for j in range(1,i):  # colmn
        i = i - 1
        print(i , end=' ')

    print()
#for i in range (n+1,0,-1):
   # for j in range(i-1,0,-1):
     #   print(j,end='')
   # print()
# output=
# 4 3 2 1
# 3 2 1
# 2 1
# 1



#6) print the pattern love
num=int(input("enter the colomn number"))
n=int(num//2)
for i in range(n):
    for j in range (n-i-1):
        print(' ',end='')
    for j in range (i+1):
        print('* ',end='')  # output first part

    if num %2==0:
        for j in range(2*(n - i - 1)):
            print(' ', end='')
    else:
        for j in range(2 * (n - i - 1)+1):
             print(' ', end='')
    for j in range(i + 1):
        print('* ', end='')  # output second part odd case include
    print()                  # output both first and second
for i in range (num,0,-1):
    for j in range (num-i):
        print(' ', end='')
    for j in range (i,0,-1):
            print('* ', end='')
    print()
# output
#    *       *
#   * *     * *
#  * * *   * * *
# * * * * * * * *
# * * * * * * * *
#  * * * * * * *
#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *


#7) print R pattern
for row in range (7):
    for col in range (5):
        if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and(col>0 and col<4)):
            print('*',end='')
        else:
            print(end=' ')
    print()
# output=
# ****
# *   *
# *   *
# ****
# *   *
# *   *
# *   *
#8) print P pattern
for row in range (7):
    for col in range (5):
        if col==0 or (col==4 and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6 )) or ((row==0 or row==3) and(col>0 and col<4)):
            print('*',end='')
        else:
            print(end=' ')
    print()
# output=
# ****
# *   *
# *   *
# ****
# *
# *
# *

#9) right angled pattern with character
n=int(input("enter the no of row :"))
k=ord("A")
for i in range (n):
    for j in range(i+1):
        print (chr(k),end=' ')
        k=k+1
    print()
    # output=
    # A
    # B C
    # D E F
    # G H I J
    # K L M N O

#10) print cross number patteren input 5
num=input("enter an odd length number")
length=len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(num[i],end='')
        else:
            print(' ',end='')
    print()
# output=
# 1       1
#  2     2
#   3   3
#    4 4
#     5
#    4 4
#   3   3
#  2     2
# 1       1


# 10) x pattern
n = int(input("enter the no of rows:"))

for i in range(n):  # rows
    for j in range(i):  # spacing
        print(' ', end=' ')
    for k in range(n - i):  # no of * print
        print('*  ', end=' ')
    print()
for i in range(1, n + 1):  # rows
    for j in range(n - i):  # spacing
        print(' ', end=' ')
    for k in range(i):  # no of * print
        print('*  ', end=' ')
    print()
    # output=
    # enter the no of rows:6
    # *   *   *   *   *   *
    #   *   *   *   *   *
    #     *   *   *   *
    #       *   *   *
    #         *   *
    #           *
    #           *
    #         *   *
    #       *   *   *
    #     *   *   *   *
    #   *   *   *   *   *
    # *   *   *   *   *   *
    #
    # 1) equlateral triangle
    n = int(input("enter the no of row :"))
    k = ord("A")
    for i in range(n):
        for j in range(n - i):
            print(" ", end='')
        for j in range(i + 1):
            print(chr(k), end=' ')
            k = k + 1
        print()

# right angled pattern with character
n = int(input("enter the no of row :"))
k = ord("A")
for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end=' ')

    print()
    # output=enter the no of row :5
    # A
    # A B
    # A B C
    # A B C D
    # A B C D E

# right angled pattern with character
n = int(input("enter the no of row :"))

for i in range(65, 65+n):
    for j in range(65, i + 1):
        print(chr(i), end=' ')

    print()
    # output=enter the no of row :5
    # A
    # B B
    # C C C
    # D D D D
    # E E E E E






















