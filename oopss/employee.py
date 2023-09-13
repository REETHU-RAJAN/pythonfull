import csv
from datetime import datetime


class Hr:
    def empoyee_creation(self):
        emp_id_ = input("ENTER THE EMPLOYEE_ID:")
        emp_id = emp_id_.upper()
        password = input("ENTER THE PASSWORD:")
        if len(password) <= 4:
            print("MIN PASSWORD LENGTH IS 4 DIGIT")
            return
        try:
            with open("employee_data.csv", 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for i in csv_reader:
                    if i['EMPLOYEE_ID'] == emp_id:
                        print("EMPLOYEE ID ALREADY ASSIGNED TO ANOTHER EMPLOYEE")
                        return
                    if i['PIN'] == password:
                        print("PASSWORD ALREADY USED BY ANOTHER EMPLOYEE")
                        return
        except Exception as e:
            print(f"error{e}")
        first_name_ = input("ENTER THE FIRST NAME:")
        first_name = first_name_.upper()
        last_name_ = input("ENTER THE LAST NAME:")
        last_name = last_name_.upper()
        address_ = input("ENTER THE ADDRESS:")
        address = address_.upper()
        mob_no = input("ENTER THE MOBILE NO:")
        if len(mob_no) != 10:
            print("ENTER A VALID MOB NO")
            return

        designation_ = input("ENTER THE DESIGNATION OF EMPLOYEE:")
        designation = designation_.upper()
        posting_location_ = input("ENTER THE POSTING LOCATION:")
        posting_location = posting_location_.upper()
        salary = input("ENTER THE CTC OF EMPLOYEE:")
        account_data = {"EMPLOYEE_ID": emp_id, "PIN": password, "FIRST_NAME": first_name, "LAST_NAME": last_name,
                        "ADDRESS": address,
                        "MOBILE_NO": mob_no, "DESIGNATION": designation, "POSTING LOCATION": posting_location,
                        "SALARY": salary}
        try:
            with open("employee_data.csv", 'a', newline="") as csvfile:
                field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                              "DESIGNATION", "POSTING LOCATION", "SALARY"]
                csv_witter = csv.DictWriter(csvfile, fieldnames=field_name)
                if csvfile.tell() == 0:
                    csv_witter.writeheader()
                csv_witter.writerow(account_data)
                print("EMPLOYEE DETAILS ADDED SUCCESSFULLY")
        except Exception as f:
            print(f"error{f}")

    def emp_del(self):
        emp_id_ = input("ENTER THE EMPLOYEE NO :")
        emp_id = emp_id_.upper()
        try:
            with open("employee_data.csv", 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            emp_found = False
            for i, account in enumerate(emp_data):
                if account["EMPLOYEE_ID"] == emp_id:
                    emp_found = True
                    del emp_data[i]
                    print("EMPLOYEE DETAILS DELETED SUCCESSFULLY")

            if emp_found:
                with open("employee_data.csv", 'w', newline="") as csvfile:
                    field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                                  "DESIGNATION", "POSTING LOCATION", "SALARY"]
                    csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                    csv_writter.writeheader()
                    csv_writter.writerows(emp_data)
                    print("DATA UPDATED SUCCESSFULLY")
            else:
                print(F"EMPLOYEE DETAILS NOT FOUND FOR THE GIVEN:{emp_id} ")
        except Exception as e:
            print(f"error{e}")

    def update_salery(self):
        emp_id = input("ENTER THE EMPLOYEE ID:")
        emp_id_upp = emp_id.upper()
        try:
            with open('employee_data.csv', 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            account_found = False
            for i, account in enumerate(emp_data):
                if account["EMPLOYEE_ID"] == emp_id_upp:
                    account_found = True
                    updated_sal = (input("ENTER THE UPDATED SALARY :"))
                    account["SALARY"] = updated_sal
                    print("SALARY UPDATED SUCCESSFULLY")

            if account_found:
                with open("employee_data.csv", "w", newline="") as csvfile:
                    field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                                  "DESIGNATION", "POSTING LOCATION", "SALARY"]
                    csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                    csv_writter.writeheader()
                    csv_writter.writerows(emp_data)
                    print("DATA UPDATED SUCCESSFULLY")
            else:
                print("ACCOUNT NOT FOUND")

        except Exception as e:
            print(f"error{e}")

    def update_designation(self):
        emp_id = input("ENTER THE EMPLOYEE ID: ")
        emp_id_upp = emp_id.upper()
        try:
            with open('employee_data.csv', 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            account_found = False
            for i, account in enumerate(emp_data):
                if account['EMPLOYEE_ID'] == emp_id_upp:
                    account_found = True
                    new_designation_ = input("ENTER NEW DESIGNATION OF EMPLOYEE:")
                    new_designation = new_designation_.upper()
                    account['DESIGNATION'] = new_designation
                    print("DESIGNATION UPDATED SUCCESSFULLY")
            if account_found:
                with open("employee_data.csv", 'w', newline="") as csvfile:
                    field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                                  "DESIGNATION", "POSTING LOCATION", "SALARY"]
                    csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                    csv_writter.writeheader()
                    csv_writter.writerows(emp_data)
                    print("DATA UPDATED SUCCESSFULLY IN DATA BASE")
            else:
                print("EMPLOYEE DETAILS NO FOUND IN DATA BASE")
        except Exception as e:
            print(f"error:{e}")

    def emp_details(self):
        emp_id = input("ENTER THE EMPLOYEE ID:")
        emp_id_upp = emp_id.upper()
        try:
            with open("employee_data.csv", "r", newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            for i, account in enumerate(emp_data):
                if account["EMPLOYEE_ID"] == emp_id_upp:
                    print(
                        f"THE EMPLOYEE DETAILS ARE EMPLOYEE NAME :{account['FIRST_NAME']},LAST NAME:{account['LAST_NAME']},ADDRESS:{account['ADDRESS']},MOB NO:{account['MOBILE_NO']},DESIGNATION:{account['DESIGNATION']},POSTING LOCATION:{account['POSTING LOCATION']},SALARY:{account['SALARY']}")
                else:
                    print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")

        except Exception as e:
            print(f"error:{e}")

    def update_first_name(self):
        emp_id_ = input("ENTER THE EMPLOYEE_ID:")
        emp_id = emp_id_.upper()
        try:
            with open("employee_data.csv", 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            account_found = False
            for i, account in enumerate(emp_data):
                if account['EMPLOYEE_ID'] == emp_id:
                    account_found = True
                    new_name_ = input("ENTER THE NEW NAME:")
                    new_name = new_name_.upper()
                    if account['FIRST_NAME'] == new_name:
                        print("NEW NAME AND OLD NAME ARE SAME")
                    else:
                        account['FIRST_NAME'] = new_name
                        print("FIRST NAME UPDATED SUCCESSFULLY")
            if account_found:
                with open("employee_data.csv", 'w', newline="") as csvfile:
                    field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                                  "DESIGNATION", "POSTING LOCATION", "SALARY"]
                    csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                    csv_writter.writeheader()
                    csv_writter.writerows(emp_data)
                    print("DATA UPDATED SUCCESSFULLY IN DATA BASE")
            else:
                print("EMPLOYEE DETAILS NO FOUND IN DATA BASE")
        except Exception as e:
            print(f"error:{e}")


class Employee:

    def emp_details(self):
        emp_id = input("ENTER THE EMPLOYEE ID:")
        emp_id_upp = emp_id.upper()
        password = input("ENTER THE PASSWORD:")
        try:
            with open("employee_data.csv", "r", newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            for i, account in enumerate(emp_data):
                if account["EMPLOYEE_ID"] == emp_id_upp and account['PIN'] == password:
                    print(f"THE EMPLOYEE DETAILS ARE EMPLOYEE NAME :{account['FIRST_NAME']},LAST NAME:{account['LAST_NAME']},ADDRESS:{account['ADDRESS']},MOB NO:{account['MOBILE_NO']},DESIGNATION:{account['DESIGNATION']},POSTING LOCATION:{account['POSTING LOCATION']},SALARY:{account['SALARY']}")
                else:
                    print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")

        except Exception as e:
            print(f"error:{e}")
    def pin_change(self):
        emp_no_=input("ENTER THE EMPLOYEE ID:")
        emp_no=emp_no_.upper()
        pin=input("ENTER THE PIN NO:")
        try:
            with open("employee_data.csv",'r',newline="")as csvfile:
                csv_reader=csv.DictReader(csvfile)
                emp_data=list(csv_reader)
            employee_found=False
            for i,account in enumerate(emp_data):
                if account['EMPLOYEE_ID']==emp_no and account['PIN']==pin:
                    employee_found=True
                    new_pass=input("ENTER THE NEW PASSWORD:")
                    if len(new_pass)>=4:
                        con_pass=input("CONFORM NEW PASSWORD:")
                        if new_pass==con_pass:
                            account['PIN']=new_pass
                            print("PASSWORD CHANGED SUCCESSFULLY")
                        else:
                            print("NEW PASSWORD AND CONFORMED PASSWORD MISMATCH")
                            return
                    else:
                        print("MIN LENGTH OF PASSWORD IS 4 DIGIT")
                if employee_found:
                    with open("employee_data.csv",'w',newline="")as csvfile:
                        field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                      "DESIGNATION", "POSTING LOCATION", "SALARY"]
                        csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                        csv_writter.writeheader()
                        csv_writter.writerows(emp_data)
                        print("DATA UPDATED SUCCESSFULLY IN DATA BASE")

                else:
                    print("EMPLOYEE DETAILS NO FOUND IN DATA BASE")

        except Exception as e:
            print(f"error:{e}")

    def mob_no_change(self):
        emp_id = input("ENTER THE EMPLOYEE ID:")
        emp_id_upp = emp_id.upper()
        password = input("ENTER THE PASSWORD:")
        with open("employee_data.csv", 'r', newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            emp_data = list(csv_reader)
        account_found = False
        for i, account in enumerate(emp_data):
            if account['EMPLOYEE_ID'] == emp_id_upp and account['PIN'] == password:
                account_found = True
                new_mob_no = input("ENTER THE NEW MOB NO:")
                if len(new_mob_no) != 10 and new_mob_no == account['MOBILE_NO']:
                    print("INVALID MOB NO/NEW MOB NO CANNOT BE SAME AS OLD MOB NO ")
                    return
                else:
                    account['MOBILE_NO'] = new_mob_no
                    print("MOB NO UPDATED ")
        if account_found:
            with open('employee_data.csv', 'w', newline="") as csvfile:
                field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                              "DESIGNATION", "POSTING LOCATION", "SALARY"]
                csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                csv_writter.writeheader()
                csv_writter.writerows(emp_data)
                print("DATA UPDATED SUCCESSFULLY")
        else:
            print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE ")

    def address_change(self):
        emp_id = input("ENTER THE EMPLOYEE ID:")
        emp_id_upp = emp_id.upper()
        password = input("ENTER THE PASSWORD:")
        try:
            with open('employee_data.csv', 'r', newline="") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                emp_data = list(csv_reader)
            account_found = False
            for i, account in enumerate(emp_data):
                if account['EMPLOYEE_ID'] == emp_id_upp and account['PIN'] == password:
                    account_found = True
                    new_address_ = input("ENTER NEW ADDRESS:")
                    new_address = new_address_.upper()
                    if new_address == account['ADDRESS']:
                        print("NEW ADDRESS AND OLD ADDRESS CANNOT BE SAME ")
                        return
                    else:
                        account['ADDRESS'] = new_address
                        print("ADDRESS UPDATED SUCCESSFULLY")
            if account_found:
                with open('employee_data.csv', 'w', newline="") as csvfile:
                    field_name = ["EMPLOYEE_ID", "PIN", "FIRST_NAME", "LAST_NAME", "ADDRESS", "MOBILE_NO",
                                  "DESIGNATION", "POSTING LOCATION", "SALARY"]
                    csv_writter = csv.DictWriter(csvfile, fieldnames=field_name)
                    csv_writter.writeheader()
                    csv_writter.writerows(emp_data)
                    print("DATA UPDATED SUCCESSFULLY IN DATA BASE ")
            else:
                print("EMPLOYEE DETAILS NO FOUND IN DATA BASE ")
        except Exception as e:
            print(f"error:{e}")


def main():
    hr = Hr()
    emp = Employee()
    print("WELCOME TO EMPLOYEE MANAGEMENT SYSTEM", datetime.today())
    while True:
        print("LOGIN OPTIONS")
        print("1-HR LOGIN")
        print("2-EMPLOYEE LOGIN")
        print("3-EXIT")
        choice = int(input("SELECT THE LOGIN OPTION:"))
        if choice == 1:
            print(" MENU")
            print("1-EMPLOYEE ID CREATION")
            print("2-EMPLOYEE SALARY UPDATION")
            print("3-EMPLOYEE DESIGNATION UPDATION")
            print("4-EMPLOYEE NAME UPDATION")
            print("5- DELETE EMPLOYEE ")
            print("6-EMPLOYEE DETAILS")
            print("7-EXIT")
            sel = int(input("PLEASE SELECT THE OPTION YOU WANT TO PERFORM:"))
            if sel == 1:
                hr.empoyee_creation()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
            elif sel == 2:
                hr.update_salery()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 3:
                hr.update_designation()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 4:
                hr.update_first_name()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 5:
                hr.emp_del()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 6:
                hr.emp_details()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
            elif sel==7:
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                break

            else:
                print("YOU HAVE SELECTED A INVALID SELECTION", datetime.today(), "HAVE A NICE DAY")

        elif choice == 2:
            print(" MENU")
            print("1-SHOW MY DETAILS")
            print("2-CHANGE MY MOBILE NUMBER")
            print("3-CHANGE MY ADDRESS")
            print("4-PIN CHANGE")
            print("5-EXIT")
            sel = int(input("PLEASE SELECT THE OPTION YOU WANT TO PERFORM:"))
            if sel == 1:
                emp.emp_details()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 2:
                emp.mob_no_change()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel == 3:
                emp.address_change()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
                # break
            elif sel==4:
                emp.pin_change()
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")

            elif sel == 5:
                print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")

            else:
                print("YOU HAVE SELECTED A INVALID SELECTION", datetime.today(), "HAVE A NICE DAY")
                break
        elif choice == 3:
            print("THANKS FOR USING EMPLOYMENT MANAGEMENT SYSTEM", datetime.today(), "HAVE A NICE DAY")
            break

        else:
            print("YOU HAVE SELECTED A INVALID SELECTION", datetime.today(), "HAVE A NICE DAY")


main()