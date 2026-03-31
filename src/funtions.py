#In this file I will create the functions that I will import into the main program.

import os

def clear():
    """
    This function is used to clean the screen every time you enter or exit a menu.
    """
 
    os.system("clear")



def student_registration():
    """
    This function is used to record the students in the system
    """

    print("--- REGISTRATION MENU ---")

    while True:
        try:
            
            student_id = int(input("\nEnter the id of the student: "))
            break
        except ValueError:
            print("\nError: Enter a valid id")  

    while True:
        try:
            name = input("Enter the name of the student: ")
            break
        except ValueError:
            print("error")
            
    while True:
        try:
          
          age = int(input("Enter the age of the student: "))
          break
        except ValueError:
            print("\nError: Enter a valid age")        

    while True:

        try:
          course = int(input("Enter the course of the student: "))
          break
        except ValueError:
            print("\nError: Enter a valid course")          
    while True:
        
          student_status = input("Enter the status of the student(active/inactive): ")
          if student_status == "active" or "inactive":
           break
          else:
           print("\nError: Enter a valid status")          

    students = {
        "student_id": student_id,
        "name":name,
        "age":age,
        "course":course,
        "student_status":student_status }
    return students

def search(record,name_search):
    """
    This function is used to search for a student using some criteria (id, name)
    """  
                
    for students in record: 
        if students['name'].strip().lower() == name_search.strip().lower():        
           return students
    return None  
    
def update_information(record):

        print("--- UPDATE MENU ---")
    
        student_update = input("\nEnter the name of the student to update: ")

        for students in record:
                
                if students['name'] == student_update:
                        print(f"\n-Student founded ✔️ : {students['name']}")
                    


                information_update = input("\n¿What information do you want to update?(Name,Id, etc): ")

                if information_update == "name":
                            try:
                                new_name = input("-Enter the new name: ")
                                students['name'] = new_name
                                print("Successfully updated student")
                                input("\nPress ENTER to exit...")
                                clear()
                                return False
                            except ValueError:
                                    print("ERROR: Enter a valid name")

                if information_update == "id":
                    try:
                     new_id = int(input("-Enter the new id: "))
                     students['student_id'] = new_id
                     print("Successfully updated student")
                     input("\nPress ENTER to exit...")
                     clear()
                     return False
                    except ValueError:
                        print("ERROR: Enter a valid id")

                if information_update == "age":
                    try:
                     new_age = int(input("-Enter the new age: "))
                     students['age'] = new_age
                     print("Successfully updated student")
                     input("\nPress ENTER to exit...")
                     clear()
                     return False
                    except ValueError:
                        print("ERROR: Enter a valid age")

                if information_update == "course":
                    try:
                     new_course = int(input("-Enter the new course: "))
                     students['course'] = new_course
                     print("Successfully updated student")
                     input("\nPress ENTER to exit...")
                     clear()
                     return False
                    except ValueError:
                        print("ERROR: Enter a valid course")

                if information_update == "status":
                    try:
                     new_status = input("-Enter the new status: ")
                     students['student_status'] = new_status
                     input("\nPress ENTER to exit...")
                     print("Successfully updated student")
                     clear()
                     return False
                    
                    except ValueError:
                        print("ERROR: Enter a valid status")

def delete_students(record):
    print("--- DELETE MENU ---")

    student_delete = input("-Enter the name of the student to delete: ")

    for students in record:
        try:
            if students ['name'] == student_delete:
                record.remove(students)
                print("STUDENT CORRECTLY ELIMINATED")
                return False
        except ValueError:
            print("ERROR: Ingresa un nombre valido")
    print(f"THE STUDENT {student_delete} DOES NOT EXIST")
    return False




        

          
