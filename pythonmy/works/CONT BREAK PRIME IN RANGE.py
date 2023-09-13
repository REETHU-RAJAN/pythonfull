
for i in range(8):
    if i==3:
        continue
    print(i)
for j in range(5):
     if j==3:
         break
     print(j)
# write a python program that prints all the numbers from 0 to 6 except 3 and 6
for i in range(0,6):
    if i==3:
        continue
    print(i)
## display from -10 to -1 in a loop
for i in range(-11,-1):
    print(i+1)
# prime number in a range
    start = int(input("enter the start range"))
    end = int(input("enter the end range"))

    print("prime number in range:", start, 'to', end)
    for i in range(start, end + 1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if (flag == 0):
            print(i, end=' ')
            # output=enter the start range1
            # enter the end range10
            # prime number in range: 1 to 10
            # 1 2 3 5 7
            # if flag==1: output=4 6 8 9 10




