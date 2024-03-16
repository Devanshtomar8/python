

# importing csv file
import csv


# Loggin Function
def login(username, password):
    with open("data.csv", "r") as file:       #gets login data from data.csv
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:     #check whether the username is present at index 0 and password is present at index 1
                return True                
    return False

# sign up
def sign_up():
    print("---------------------------------------------------------------")
    print("                             Sign UP                           ")
    print("---------------------------------------------------------------")
    # Ask for username and password for new admin
    user_name=input("Enter User Name: ")
    password=input("Enter Password: ")
    # append new data in data.csv
    with open("data.csv",mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([user_name,password])

        


# ADD Faculty
def add_faculty():
    print("---------------------------------------------------------------")
    print("             Registration Form for New faculty                 ")
    print("---------------------------------------------------------------")
    # ask for neccessary information of new faculty
    name=input("Enter Full name: ")
    gender=input("Enter Gender: ")
    age=int(input("enter age: "))
    email=input("Enter email: ")
    phone=int(input("Enter phone number: "))
    address=input("Enter Address: ")
    department=input("Enter department: ")
    salary=float(input("Enter Salary: "))
    # append new faculty details in the faculty.csv at sepcific index
    with open("faculty.csv",mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([name.upper(),gender.upper(),age,email.upper(),phone,address.upper(),department.upper(),salary])



# Update a faculty
def update_faculty():
    print("---------------------------------------------------------------")
    print("                     Update faculty details                    ")
    print("---------------------------------------------------------------")
    
    while True:
        # ask for faculty name for updation
        name=input("enter faculty name: ")
        name=name.upper()

        found=0     # to check if name is in the file or not
        with open('faculty.csv',mode='r') as f:
            csvr=csv.reader(f)
            my_list=[]
            for r in csvr:
                if r[0]==name:
                    print("1. Change Name\n2. Change Genders\n3. Change Age\n4. Change Email\n5. Change phone number\n6. Change Address\n7. Change Department\n8. Chnage Salary ")
                    try:
                        choice=int(input("Enter choice: "))
                    except ValueError:
                        print("warning..! Please enter only numbers")
                    if choice==1:
                        a=input("Enter name: ")
                        r[0]=a.upper()
                    elif choice==2:
                        a=input("Enter Gender: ")
                        r[1]=a.upper()
                    elif choice==3:
                        r[2]=input("Enter Age: ")
                    elif choice==4:
                        a=input("Enter Email: ")
                        r[3]=a.upper()
                    elif choice==5:
                        r[4]=int(input("Enter Phone Number: "))
                    elif choice==6:
                        a=input("Enter Adress: ")
                        r[5]=a.upper()
                    elif choice==7:
                        a=input("Enter Department: ")
                        r[6]=a.upper()
                    elif choice==8:
                        r[7]=float(input("Enter Salary: "))
                    else:
                        print("Invalid Operation...!")
                    found=1
                my_list.append(r)
            f.close()
        if found==0:
            print("Their is no faculty with name",name)
        else:
            with open('faculty.csv','w',newline='') as f:
                csvr=csv.writer(f)
                csvr.writerows(my_list)
                print("Data Updated successfully !!!")
                f.close()
        #ask whether user want to continue updation or not
        if input("Want to Continue Updation? (y/n): ") not in "yY": 
                break


# Search faculty by name or email
def search_faculty():
    print("---------------------------------------------------------------")
    print("                         Search Faculty                        ")
    print("---------------------------------------------------------------")
    name=input("Enter faculty name or email: ")
    name=name.upper()
    with open('faculty.csv', 'r') as f:
        csvr = csv.reader(f)
        found = False   # to check if name is in the file or not
        for r in csvr:
            # fetching and print the detail of specific faculty
            if r[0]==name or r[3]==name:
                print(f"Faculty Name: {r[0]}\nGender: {r[1]}\nAge: {r[2]}\nEmail: {r[3]}\nPhone: {r[4]}\nAddress: {r[5]}\nDepartment: {r[6]}\nSalary: {r[7]}")
                found = True
        if not found:
            print("Faculty not found.")




# print all faculty details
def view_faculty():
    print("---------------------------------------------------------------")
    print("                      All Faculty Details                      ")
    print("---------------------------------------------------------------")
    with open('faculty.csv', 'r') as f:
        csvr = csv.reader(f)
        print("Faculty Details:")
        # printing all the faculty details row-wise
        for r in csvr:
            print(f"{r[0]}\t\t{r[1]}\t\t{r[2]}\t\t{r[3]}\t\t{r[4]}\t\t{r[5]}\t\t{r[6]}\t\t{r[7]}")




# delete specific faculty by name
def delete_faculty():
    print("---------------------------------------------------------------")
    print("                         Delete Faculty                        ")
    print("---------------------------------------------------------------")
    name=input("Enter name: ")
    name=name.upper()
    with open('faculty.csv', 'r') as f:
        csvr = csv.reader(f)
        found=False
        rows = list(csvr)

    #removing the all the details of specific faculty
    for i, r in enumerate(rows):
        if r[0] == name:
            del rows[i]
            found=True
            break
        
    # rewriting all the details again
    with open('faculty.csv', 'w', newline='') as f:
        csvw = csv.writer(f)
        csvw.writerows(rows)
        print("Faculty with tha name",name,"deleted successfully")

    if not found:
            print("Faculty not found.")










