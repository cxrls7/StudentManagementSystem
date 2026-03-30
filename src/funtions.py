#In this file I will create the functions that I will import into the main program.

import os

def pause():
    """
    This function is used to pause the program while you are in the menu
    """
    input("Press ENTER to return to the main menu...")
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
            print("\nError: Ingrese un id valido")  

    while True:
        try:
          
          name = str(input("Enter the name of the student: ")) 
          break
        except ValueError:
            print("\nError: Ingrese un nombre valido")     

    while True:
        try:
          
          age = int(input("Enter the age of the student: "))
          break
        except ValueError:
            print("\nError: Ingrese una edad valida")        

    while True:

        try:
          course = int(input("Enter the course of the student: "))
          break
        except ValueError:
            print("\nError: Ingrese un curso valido")          
    while True:
            
        try:
          student_status = input("Enter the status of the student(active/inactive):  ")
          break
        except student_status != "active" or "inactive":
              print("\nError: Ingrese un valor valido")          

    students = {
        "student_id": student_id,
        "name":name,
        "age":age,
        "course":course,
        "student_status":student_status
    }
    return students

                
                
    
     
