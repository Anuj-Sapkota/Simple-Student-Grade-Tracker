# Objective:
# Create a Python program that manages student grades using a CSV file. The program should allow users to:
# ✅ Add new student records
# ✅ View all student records
# ✅ Search for a student by name or ID
# ✅ Update a student’s grade
# ✅ Delete a student’s rp
import csv

def add_student_records():
    try:
        id = int(input("Enter the student's id: "))  
        name = input("Enter the student's name: ")
        subject = input("Enter the subject's name: ")
        grade = input("Enter the student's grade: ")


        with open('grades.csv', mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id, name, subject, grade])
            file.close()  
    except:
        print("❌Please enter the correct Id.")  
        
    
def view_student_records():
    print("\n\n")
    with open('grades.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:<5} {header[1]:<18} {header[2]:<10} {header[3]:<3}")
        print('-'*36)
        for row in reader:
            print(f"{row[0]:<5} {row[1]:<18} {row[2]:<10} {row[3]:<3}")
        file.close()

def search_student():
     name = None
     id = 0
     isFound = True
     print("\nSearch by id or name".center(20,'='))
    
     search_choice = input("Enter the id or name of the student:")
     try:
        int(search_choice)
        id = search_choice
     except:
        name = search_choice

        with open('grades.csv', mode='r', newline="") as file:
            reader = csv.reader(file)
            next(reader) # skips the title header
            for row in reader:
                if row[0] == id or row[1] == name:
                    print("\n")
                    print('-'*36)
                
                    print(', '.join(row))
                    print('-'*36)
                    isFound = True
                else:
                    isFound = False
            
        if isFound == False:
            print("❌Row not Found, Try again!")


def update_student_record():
    isFound = True
    choice = input("Enter the id of the student whose record is to be updated: ")
    updated_rows = []
    with open('grades.csv', mode='r', newline="") as file:
         reader = csv.reader(file)
         header = next(reader)
         for row in reader:
             if row[0] == choice:
                 print(f"\n{header[0]:<5} {header[1]:<18} {header[2]:<10} {header[3]:<3}")
                 print('-'*40)
                 print(f"{row[0]:<5} {row[1]:<18} {row[2]:<10} {row[3]:<3}")

                 subject = input("Enter the new subject: ")
                 grade = input("Enter the new grade: ")
                 row[2] = subject
                 row[3] = grade
                 isFound = True
             else:
                 isFound = False 
             updated_rows.append(row)
    if isFound == True:
        with open('grades.csv', mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        
        print("\n✅Records updated successfully")
    else:
        print("❌Row not Found, Try again!")

def delete_student_record():
    delete_choice = input("Enter the id of the student whose records you want to delete: ")
    isFound = True
    updated_student_record = []
    with open('grades.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        for rows in reader:
            if rows[0] == delete_choice:
                try:
                    choice = int(input("Are you sure you want to delete this row?\n1. Yes\n2. No\n"))
                    if choice == 1:
                        isFound = True
                        continue
                except:
                    print("Wrong Choice! Please enter the number from the option given!")
            else:
                updated_student_record.append(rows)
                isFound = False
    if isFound == True:            
        with open('grades.csv', mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_student_record)
            print("Record deleted successfully!")
    else:
        print("❌Row not Found, Try again!")

while True:
    print("\n\n")
    print("Student Grade Tracker".center(36,'='))
    print("1. Add new Students\n2. View all student records\n3. Search for a Student by name or ID\n4. Update a student's grade\n5. Delete a student's record\n6. Exit")
    try:
        choice = int(input("Enter your choice number: "))
    except:
        print("\n❌Invalid option selected! Please try again")
        continue
    if (choice==1):
        add_student_records()
    elif choice == 2:
        view_student_records()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student_record()
    elif choice == 5:
        delete_student_record()
    elif choice == 6:
        exit()
    else:
        print("\n❌Invalid option selected! Please try again")
    # Functions
  
    

    

