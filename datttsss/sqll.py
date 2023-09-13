
# class QueueUsingStacks:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self, value):
#         self.stack1.append(value)
#
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#
#         if not self.stack2:
#             return None
#
#         return self.stack2.pop()
#
# # Test the Queue using Stacks implementation
# queue = QueueUsingStacks()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# print(queue.dequeue())  # Output: 1
# print(queue.dequeue())  # Output: 2
# print(queue.dequeue())  # Output: 3
# print(queue.dequeue())  # Output: None (queue is empty)

# queue = []
# def en_queue():
#     element = int(input("Enter element:"))
#     queue.append(element)
#     print(element,"is added to the Queue")
# def de_queue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         e=queue.pop(0)
#         print(e,"is removed from queue")
# def display():
#     print(queue)
#
# while True:
#     select = input("enter ur choice:1.add 2.remove 3.display 4.quit\n")
#     if select=='1':
#         en_queue()
#     elif select=='2':
#         de_queue()
#     elif select=='3':
#         display()
#     elif select=='4':
#         break
#     else:
#         print("invalid operation")

# class Node:
#     def _init_(self,data):
#         self.data = data
#         self.ref = None
#
# class linked_list:
#     def _init_(self):
#         self.head = None
#     def print_ll(self):
#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data, "--->", end='')
#                 n= n.ref
#
#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.ref=self.head
#         self.head=new_node
#
#     def add_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n=n.ref
#             n.ref=new_node
#
#     def add_bet(self,data,x):
#         n=self.head
#         while n is not None:
#             if x==n.data:
#                 break
#             n=n.ref
#         if n is None:
#             print("item not found")
#         else:
#             new_node=Node(data)
#             new_node.ref=n.ref
#             n.ref=new_node
#     def del_begin(self):
#         if self.head is None:
#             print("Empty")
#         else:
#             self.head=self.head.ref
#     def del_end(self):
#         if self.head is None:
#             print("Empty")
#         else:
#             n=self.head
#             while n.ref.ref is not None:
#                 n=n.ref
#             n.ref=None
#     def del_value(self,x):
#         if self.head is None:
#             print("Empty")
#             return
#         if x== self.head.data:
#             self.head=self.head.ref
#             return
#         n=self.head
#         while n.ref is not None:
#             if x == n.ref.data:
#                 break
#             n=n.ref
#         if n.ref is None:
#             print("Node is not present")
#         else:
#             n.ref=n.ref.ref
#
#
# 10)
# ll.add_begin(20)
# ll.add_begin(30)
# ll.add_end(100)
# ll.add_bet(200,20)
# #ll.del_begin()
# #ll.del_end()
# #ll.del_value(10)
# ll.print_ll()
#
# ll = linked_list()
# ll.add_begin()


