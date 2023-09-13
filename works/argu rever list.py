#diff arguments
#position arguments
def lap(name,model,color):
    print("lap details:",name,model)
lap("del",5,"black")
#arbitary keyword argument
def lap(**keywor):
    print("lap details:",keywor["name"],keywor["model"],keywor["color"])
lap(name='del',model=5,color="black")

#arbitary position arguments
def lap(*args):
    print("name:",args)
lap("del",5,"black")
#keyword argument
def lap(lap1,lap2,lap3):
    print("the latest lap"+lap3)
lap(lap1="micro",lap2="hp",lap3="del")


#default value
def country(country='india'):
     print("iam from "+country)
country()
country("italy")
country("usa")
# reverse using function

string="python"
s=list(string)
s.reverse()
#print(s)
print(''.join(s))

def reverse(string):
    s=list(string)
    s.reverse()
    print("".join(s))

string="python"
reverse(string)
string='reethu'
reverse(string)
#reverse without slicing
def reverse(string):
    s=''
    for i in string:
        s=i+s
        print(s)
string='python'
reverse(string)
#list comprehension reverse
str="you are awesome"
string=[str[i] for i in range(len(str)-1,-1,-1)]
print(''.join(string))
