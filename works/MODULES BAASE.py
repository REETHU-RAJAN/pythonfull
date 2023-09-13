# #modules
# a python module can be defined as a python program file which contains a python code including python functions,class or variables.
# python  code file saved with the extension(.py) is treated as the module.lambda we may have runnable code inside the python module
# modules in python provides us the flexibility to organize the code in a logical way.
# to use the fuctionality of one module into another, we must have to import the specific module>
#1  user defined module


#import june15
#from june15 import sum
#print(sum(4,6))

#2  build in module

import math
print(math.sqrt(5))
print(math.factorial(5))
print(math.pi)
r=5
print(math.pi*r*r)
# 3  os module

# operate s/m task work avan  it is possible to automatically perform many os tasks.
# the os module in python provides fn for creating and removing a directory(folder)
#     fecting its contents,

import os
#os.mkdir(r"C:\Users\admin\PycharmProjects\pythonmy\works\juu") # make
#os.rmdir(r"C:\Users\admin\PycharmProjects\pythonmy\works\juu")] # remove
#print(os.getcwd()) # current work get
#os.chdir('D:/')  # change directory
#print(os.getcwd())

#4  random module
import random
print(random.randrange(10))
print(random.randint(1,100))
a=[1,2,3,4]
(random.shuffle(a))
print(a)
str='computer'
print(random.choice(str))
print()
#5  date time module

import datetime
from datetime import date
today=date.today()
print("today date is:",today)

now=datetime.datetime.now()
print(now)
now=datetime.datetime.now()
current_time=now.strftime("%H:%M:%S")
print(current_time)
# 6 json module # storing amd exchanging of data
import json # javascript object notation
x={"name":"reethu","age":12}
print(type(x))
y=json.dumps(x) #python to json (dict to string)
print(y)
print(type(y))
x='{"name":"reethu","age":12}'
print(type(x))

y=json.loads(x) #json to python (string to dict)
print(y)
print(type(y))
func=dir(json)
print(func)

# fecting second value from json
import json
x='{"name":"reethu","age":12,"course":"python"}'
y=json.loads(x)
print(y["age"])

#access the nested key "salery "from json
import json
samplejson='''{
 "company":{
   "employee":{
     "name":"emma",
     "payble":{
       "salary":7000,
       "bonus":800
     }
   }
 }
}'''
y=json.loads(samplejson)
print(y["company"]["employee"]["payble"]["salary"])

#write a python program to generate a random color hex,a random alphabetical string,random value b/w 2 integers
#(inclusive) and a random multiple of 7 b/w 0 and 70.use random.randint()
import random
color="#%06x" % random.randint(0,0xFFFFFF)
print(color)
print(random.randint(1,100))
str='computer'
print(random.choice(str))
print(random.randint(1,10)*7)
print(random.randint(1,50)*5)


