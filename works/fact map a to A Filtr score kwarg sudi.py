## ** based
class car( ):
     def __init__(self,**kwargs):
         self.speed=kwargs['s']
         self.color=kwargs['c']
audi = car(s=200,c='red')
bmw = car(s=250,c='black')
mp = car(s=120,c='white')
print(audi.color)
#* based
class car():
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]


audi = car(200, 'red')
bmw = car(250, 'black')
mp = car(120, 'white')
print(audi.color)
# small to capital map

persons=['ab','bc']
uppered_person=list(map(str.upper,persons))
print(uppered_person)
# filer score
scores=[67,99,80,54,87]
def is_a_student(score):
    return score>=80
passing = list(filter(is_a_student,scores))
print(passing)
 #factorial of number
num = int(input("enter a number"))
f = 1
i = 1
while (i <= num):

    f = f * i
    i = i + 1

print("factoial of number:", f)

def fa_n(nums):
    f=1
    i=1
    for i in (nums):
        f = f * i
        i= i+1
        print(f)
    return (" ")
nums=int(input("enter a number:"))
print(fa_n(nums))

