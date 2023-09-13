# python program to print even and odd num in an array
from array import *
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print("array length:",len(arr))
for i in range(len(arr)):
    if (arr[i]%2==0):
        print(arr[i],end=' ')
print('\n')
for i in range(len(arr)):
    if (arr[i]%2!=0):
        print(arr[i],end=' ')
# insertion of array elements
arr=[0,0,0]
arr[0]=1
arr[1]=2
arr[2]=3
print("array elements:",arr)
#op:array elements: [1, 2, 3]
print("-------------------------")
# another method using import module
from array import*
array2=array('i',[10,20,30])
array2.pop(1)
print('array delection')
for x in array2:
    print(x,end='')


    print('\n-------------------------------------------')
#searching of array elements
print("search array element(display index postion)")
print(array2.index(10))

print("\n--------------------")
# update array
print("update array")
array2[0]=70
for x in array2:
    print(x,end='')
    print('\n----------------------------------')
#append array
print("append")
array2.append(90)
for x in array2:
    print(x,end='')
    print('\n--------------------')


""" working of stack 
1.a pointer called TOP is used to keep track of the top element in the stack
2. when initializing the stack,we set its value to -1 so that we can check if the stack is empty
by comparing TOP==-1
3.on pushing an element,we increase the value of TOP and place the new element in the position pointed to by TOP.
4.on popping an element,we return the element pointed to by TOP and reduce its value
5.Before pushing,we check if the stack is already full
6.Before popping,we check if the stack is already empty"""

# in the following program, we implement it as add and remove fn .we declare an empty list and use the append() and pop() methods
stack=[]
def push_element():
    element=input("enter the element:")
    stack.append(element)
    print(element,"is added to the stack")
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(e,"is removed from the stack")
def top_element():
    top=stack[-1]
    print("top of the stack is",top)
def display_stack():
    print(stack)
while True:
    choice=input("enter the choice:1.push 2.pop 3.top 4.display 5.quit\n")
    if choice=='1':
        push_element
    elif choice=='2':
        pop_element()
    elif choice=='3':
        top_element()
    elif choice=='4':
        display_stack()
    elif choice=='5':
        break
    else:
      print("invalid operation")



#create a stack
def create_stack():
    stack=[]
    return stack
# create an empty stack
def check_empty(stack):
    return len(stack)==0
#adding item into the stacks
def push(stack,items):
    stack.append(items)
    print("pushed items:"+ items)
#removing an element from stack
def pop(stack):
    if (check_empty(stack)):
        return "empty"
    return stack.pop()
stack=create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
print("popped item:"+ pop(stack))
print("stack after popping an element :" + str(stack))
print("\n-----------------------------------------")
# Python Script to Implement two stacks in a list
import math


class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = math.floor(n / 2) + 1
        self.top2 = math.floor(n / 2)

    # Method to push an element x to stack1

    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow by element : ", x)

    # Method to push an element x to stack2

    def push2(self, x):

        # There is at least one empty space for new element
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow by element : ", x)

    # Method to pop an element from first stack

    def pop1(self):
        if self.top1 <= self.size / 2:
            x = self.arr[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    # Method to pop an element from second stack

    def pop2(self):
        if self.top2 >= math.floor(self.size / 2) + 1:
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


# Driver program to test twoStacks class
if __name__ == '__main__':
    ts = twoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is : " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is : " + str(ts.pop2()))
print("\n---------------------------------------")
# demonstrate
# queue
# implementation
# using list

# Initializing a queue
queue=[]
def en_queue():
    element=input("enter the element:")
    queue.append(element)
    print(element,"is added to the queue")
def de_queue():
    if not queue:
        print("stack is empty")
    else:
        e=queue.pop(0)
        print(e,"is removed from the queue")
def show_queue():

    print(queue)

while True:
    choice=input("enter the choice:1.add 2.remove 3.show 4.quit\n")
    if choice=='1':
        en_queue()
    elif choice=='2':
        de_queue()
    elif choice=='3':
        show_queue()
    elif choice=='4':


        break
    else:
      print("invalid operation")
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty