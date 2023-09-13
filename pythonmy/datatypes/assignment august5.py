"""1.Ask the user to enter the names of three people they want to invite to a party and store them
 in a list. After they have entered all three names, ask them if they want to add another. If they do,
 allow them to add more names until they answer “no”. When they answer “no”, display how many people
 they have invited to  the party."""
people=[]
print('Enter name of three people:')
for i in range(0,3):
    name=input()
    people.append(name)
print(people)
def add_another():
    add_name=input()
    people.append(add_name)
def display():
    print(people)
while True :
    ask=input('If you wants to add another:')
    if ask=='yes':
        add_another()
    elif ask=='no':
        display()
        break
    else:
        print('invalid')

'''Enter name of three people:
reethu
rajan
ragil
['reethu', 'rajan', 'ragil']
If you wants to add another:yes
shyla
If you wants to add another:no
['reethu', 'rajan', 'ragil', 'shyla']'''





"""2.Change the above question so that once the user has completed their list of names, display the full 
list a
nd ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they answer
 “no”, delete
that entry from the list and display the list again."""



people=[]
print('Enter name of three people:')
for i in range(0,3):
    name=input()
    people.append(name)
print(people)
def add_another():
    add_name=input()
    people.append(add_name)
def display():
    print(people)

while True :
    ask=input('If you wants to add another:')
    if ask=='yes':
        add_another()
    elif ask=='no':
        display()
        break
    else:
        print('invalid')
one_name=input('Enter one name from the list:')
for i in people:
    if i==one_name:
        print(f'Position of {one_name} in the list is:',people.index(one_name))
        while True:
            entry=input('If you want to come this person to the party:')
            if entry=='no':
                people.remove(one_name)
                print(people)
                break
            else:
                print(people)
                break

"""Enter name of three people:
rr
ee
tt
['rr', 'ee', 'tt']
If you wants to add another:no
['rr', 'ee', 'tt']
Enter one name from the list:ee
Position of ee in the list is: 1
If you want to come this person to the party:no
['rr', 'tt']

Process finished with exit code 0
"""


"""3.Using the below list ask the user which row they would like displayed and display just that row.
 Ask the
m to enter a new value and add it to the end of the row and display the row again. list=[[2,5,8],[3,7,4],
[1,6,
9],[4,2,0]]"""




list_1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
ask=int(input('Enter which row you would like to displayed:'))
print(list_1[ask])
new_list=list_1[ask]
new_val=int(input('Enter a new value to the row:'))
new_list.append(new_val)
print('After appending:',new_list)

"""Enter which row you would like to displayed:2
[1, 6, 9]
Enter a new value to the row:4
After appending: [1, 6, 9, 4]"""
"""
4.Ask the user to enter the name, age and Id for four people. Ask for the name of one of the people in the
list and display their age and Id."""

persons=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    persons.append({"name":name,"age":age,"id":id})

display=input("Enter the name of the person from the list: ")
for p in persons:
    if p["name"]==display:
        print(f"Age: {p['age']},ID:{p['id']}")


"""Enter your name: re
Enter your age: 12
Enter your id: 1
Enter your name: ff
Enter your age: 45
Enter your id: 2
Enter your name: tt
Enter your age: 43
Enter your id: 3
Enter your name: uu
Enter your age: 66
Enter your id: 4
Enter the name of the person from the list: uu
Age: 66,ID:4"""















""""
5.Adapt the above program to display the names and ages of all the people in the list but do not show 
their Id."""

persons=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    persons.append({"name":name,"age":age,"id":id})

for p in persons:
    print(f"Name: {p['name']}, Age:{p['age']}")


"""Enter your name: re
Enter your age: 3
Enter your id: 1
Enter your name: ee
Enter your age: 4
Enter your id: 2
Enter your name: rew
Enter your age: 6
Enter your id: 3
Enter your name: nn
Enter your age: 7
Enter your id: 4
Name: re, Age:3
Name: ee, Age:4
Name: rew, Age:6
Name: nn, Age:7"""




"""
6.a. Create a dictionary representing a library catalog with book titles as keys and values as 
dictionaries containing information like author, publication year, and genre.
b. Add a new book to the catalog and update the author of an existing book.
c. Write a function to count how many books in the catalog were published before a given year"""


books={
    "The Pregnancy Bible":{"author":"KAREENA","publication year":2022,"genre":"FANTACY"},
    "Will":{"author":"WILLSMITH","publication year":2002,"genre":"COMEDY"},
    "The Great Big Lion":{"author":"JJ","publication year":1999,"genre":"Historical"},
    "It’s a Wonderful Life":{"author":"KK","publication year":2000,"genre":"Historical"},

}
# Add a new book to the catalog
newbook={"The 7 Sins of Being a Mother":{"author":"Tahira Kashyap Khurrana","publication year":1994,"genre":"portrait"}}
books.update(newbook)
print("New book added: ",books,"\n")

# update the author of an existing book
for k,v in books.items():
    if k=="Will":
        v["author"]="PPS"
print("Author updated: ",books,"\n")

# Write a function to count how many books in the catalog were published before a given year.
def yearcount(years,date):
    count = 0
    for y in years:
        if y < date:
            count += 1
    return count
years=[]
for b,v in books.items():

    years.append(v["publication year"])
count=yearcount(years,2000)
print("Books that published before 2020:",count)


"""New book added:  {'The Pregnancy Bible': {'author': 'KAREENA', 'publication year': 2022, 'genre': 'FANTACY'}, 'Will': {'author': 'WILLSMITH', 'publication year': 2002, 'genre': 'COMEDY'}, 'The Great Big Lion': {'author': 'JJ', 'publication year': 1999, 'genre': 'Historical'}, 'It’s a Wonderful Life': {'author': 'KK', 'publication year': 2000, 'genre': 'Historical'}, 'The 7 Sins of Being a Mother': {'author': 'Tahira Kashyap Khurrana', 'publication year': 1994, 'genre': 'portrait'}} 

Author updated:  {'The Pregnancy Bible': {'author': 'KAREENA', 'publication year': 2022, 'genre': 'FANTACY'}, 'Will': {'author': 'PPS', 'publication year': 2002, 'genre': 'COMEDY'}, 'The Great Big Lion': {'author': 'JJ', 'publication year': 1999, 'genre': 'Historical'}, 'It’s a Wonderful Life': {'author': 'KK', 'publication year': 2000, 'genre': 'Historical'}, 'The 7 Sins of Being a Mother': {'author': 'Tahira Kashyap Khurrana', 'publication year': 1994, 'genre': 'portrait'}} 

Books that published before 2020: 2"""
