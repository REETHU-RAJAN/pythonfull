# 1)print a pattern pyramind
n=int(input("enter a number"))


for i in range (n+1):# rows
    for j in range(n-i):#spacing
        print(' ',end=' ')
    for k in range (i):#no of * print
        print('*  ',end=' ')
    print()
    # output=
    #       *
    #     *   *
    #   *   *   *
    # *   *   *   *
   # 2)CREATE inverted full pyramid pattern
n = int(input("enter a number"))


for i in range(n + 1):  # rows
    for j in range(i):  # spacing
        print(' ', end=' ')
    for k in range(n - i):  # no of * print
        print('  *', end=' ')
    print()
# output=
#   *   *   *   *   *   *   *
#     *   *   *   *   *   *
#       *   *   *   *   *
#         *   *   *   *
#           *   *   *
#             *   *
#               *
#

   # 3)number pyramid
n = int(input("enter a number"))


for i in range(n + 1):  # rows
    for j in range(i):  # spacing
        print(' ', end=' ')
    for k in range(n - i):  # no of * print
        print(i, end='   ')
    print()
    # enter a number5
# 0   0   0   0   0
# 1   1   1   1
#   2   2   2
#   3   3
#      4


 #4) numberrr
n = int(input("enter a number"))

for i in range(n + 1):  # rows
    for j in range(n - i):  # spacing
        print(' ', end=' ')
    for k in range(i):  # no of * print
        print(k, end='   ')

    print()
        #    0
        #   0 1
        #  0 1 2
        # 0 1 2 3

#5) number
n = int(input("enter a number"))

for i in range(n + 1):  # rows
    for j in range(n - i):  # spacing
        print(' ', end=' ')
    for k in range(i):  # no of * print
        print(i, end='   ')
        i = i + 1
    print()
# output=6
 #           1
 #         2   3
 #       3   4   5
 #     4   5   6   7
 #   5   6   7   8   9
 # 6   7   8   9   10   11

 #6) nummmmmmm
n=int(input("enter a number"))


for i in range (n+1):# rows
    for j in range(n-i):#spacing
        print(' ',end=' ')
    for k in range (i):#no of * print
        print(i,end='  ')
    print()

    # output=
    #       1
    #     2  2
    #   3  3  3
    # 4  4  4  4

#7) phh
n=int(input("enter a number"))
i=1
k=1

while i<=n:
    j=1
    while j<=i:
        print( k , end='  '),
        j+=1
        k+=1
    print( )
    i+=1
#) output=
# 1
#2  3
#4  5  6
#7  8  9  10
#10) print cross number patteren input 5
num=input("enter an odd length number")
length=len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(num[j],end='')
        else:
            print(' ',end='')
    print()
# output= 12345
# 1   5
#  2 4
#   3
#  2 4
# 1   5
#11) print cross number patteren input 5
num=input("enter an odd length number")
length=len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(num[i],end='')
        else:
            print(' ',end='')
    print()
# output= enter an odd length number12345
# 1   1
#  2 2
#   3
#  4 4
# 5   5

# hollow patteren in case of odd number
n=int(input("enter an odd number:"))
for row in range(n):
    for col in range (n):
        if row+col==(n//2) or col-row==(n//2) or row-col==(n//2) or row+col==3*(n//2):
            print("* ",end='')
        else:
            print(' ',end='')
    print()

# output=
#     *
#    *  *
#   *    *
#  *      *
# *        *
#  *      *
#   *    *
#    *  *
#     *

