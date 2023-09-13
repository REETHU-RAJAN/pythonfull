#question:1
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines=[]
while True:
      str1=input()
      if str1=='':
            break
      else:
            lines.append(str1+'\n')
print(lines)
x=' '.join(lines)
print(x)
for i in x:
    capt=x.upper()
print(capt)
# Question:2
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡¬Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
x=int(input("enter the number of rows:"))
y=int(input("enter the number of colomn:"))
a=[[i*j for j in range(y)] for i in range(x)]
print(a)
# Question:3
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
s =input("enter the sequence:")
d={"DIGITS":0, "LETTERS":0}  #letters=0 digits=0
for c in s:
     if c.isdigit():
         d["DIGITS"]+=1 #digits+=1
     elif c.isalpha():
         d["LETTERS"]+=1 #alpha or numeric+=1

print("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])


# Question:4
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
s =input("enter the sequence:")
d={"upper":0, "lower":0}
for c in s:
     if c.isupper():
         d["upper"]+=1
     elif c.islower():
         d["lower"]+=1

print("upper", d["upper"])
print ("lower", d["lower"])

# Question:5
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
values = input("ENTER THE NUMBERS:")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))

# Question:6
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

values = []
for i in range(1000, 3001):
      s = str(i)
      if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
         values.append(s)
print(",".join(values))
