
def sum(a,b):
    return (a+b)
print ("c=",(sum(10,20)))

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "ridhay", lname = "Reethu")

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("ridhay", "Reethu")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "ridhay", child2 = "reethu", child3 = "sai")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("ridhay", "reethu", "sai")

def my_function(fname):
  print(fname + " Reethu")

my_function("ridhay")
my_function("sai")
# lambda
x = lambda a : a + 10
print(x(5))
#local
def myfunc():
  x = 300
  print(x+25)
myfunc()

#global
x = 300
def myfunc():
  print(x+25)
myfunc()

#count upper and lower
def string_count(s):
    d={'uppercase':0, "lowercase":0}
    for c in s:
        if c.isupper():
           d["uppercase"]+=1
        elif c.islower():
           d["lowercase"]+=1
        else:
           pass
    print("orginal string:", s)
    print("no. of uppercase:",d["uppercase"])
    print("no. of lowercase:", d["lowercase"])
string_count('reeTHU is MOTHER of 2 BABIES')

# LEAP YR
def leap_or_not(year):
    if((year % 4==0) and (year % 100!=0) or (year % 400==0)):
          print("its leap year")
    else:
          print("not leap year")
year=int(input("eneter a year"))
leap_or_not(year)

#perfect number
