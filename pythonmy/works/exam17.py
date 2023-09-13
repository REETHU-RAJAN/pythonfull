# fecting second value from json
import json
x='{"name":"reethu","age":12,"course":"python"}'
y=json.loads(x)
print(y['age'],y['course'])

import random

str='computer,hiii'
print(random.choices(str))
#print()

lines=[]
while True:
    s1=input()
    if s1:
        lines.append(s1.upper())
    else:
        break;
for s1 in lines:
  print(s1)
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("turtle")
skk=turtle.Turtle()
skk.forward(100)
turtle.done()
