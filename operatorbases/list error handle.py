lst=[10,20,30,40,50]
location=int(input("enter location to fetch value from list"))
try:

   print(lst[location])
except Exception as e:
    # location = int(input("enter location to fetch value from list"))
    # try:
    #    print(lst[location])
    #
    # except Exception as e:


    print(e.args)
finally:# sure case mandatory cases must work this
     print("db commit 1")
     print("file read")