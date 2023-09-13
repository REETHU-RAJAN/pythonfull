#1) write a program to check a character is vowel or not
a=input("enter any character:")
vowels="aeiouAEIOU"
if a in vowels:
    print("entered character is vowel")
else:
    print("entered character is not vowel")
# seperate vowels and consonat
a=input("enter any character:")
vowels="aeiouAEIOU"
x=[]
y=[]
for i in a:
    if i in vowels:
        x.append(i)
    else:
        y.append(i)
print("vowels",x)
print("consont",y)
#........................................................

#2) accept the electric units from the user and calculate the bill according to the following rates.
#first 100 units: free, next 200 units: rs2 per day, above 300 units : rs 5 per day, if number of units is 500 then total bill + 0+400+1000=1400

unt=int(input("enter number of units:"))
if unt<=100:
    amt=0
elif unt>100 and unt<=300:
    amt=(unt-100)*2
else:
    amt=400+(unt-300)*5
print("total amount to pay is:",amt)
#..........................................................
#3)accept th kilometers covered and calculate the bill according to the following criteria: first 10km: rs 11/km , next 90 km:rs 10/km, after that: rs 9/km
kms=int(input("enter the kms covered:"))
if kms<=10:
    amt=kms*11
elif kms >10 and kms <= 100:
    amt = 110+ (kms-10)*10
elif kms > 100:
    amt = 1010+(kms-100)*9
print("total amount to pay is",amt)