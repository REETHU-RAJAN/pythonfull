import csv
with open("data.csv",'r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

    file.close()

# list format
with open("smple_data.csv",'w')as file:
    writer=csv.writer(file)
    writer.writerow(["s.no","name"])
    writer.writerow(['1','priya'])
    file.close()
with open("smple_data.csv",'r',newline='\n')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

# dictionary format

with open("smple_data.csv",'w',newline='')as csvfile:
    fieldnames=["firstname","lastname","age","year"]
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({"firstname":"reethu","lastname":"rajan","age":28,"year":2023})
    writer.writerow({"firstname": "ragil", "lastname": "rajan", "age": 35, "year": 1994})
    csvfile.close()
with open("smple_data.csv",'r')as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        print(row)



