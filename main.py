from src.funtions import student_registration, clear, search,update_information,delete_students

def main():
    """
    This function is used to create the main menu to the program
    """
    record = []
    while True:
        print("--- WELCOME TO THE STUDENT MANAGEMENT SYSTEM ---")
        print("\nSystem used to record the information of the students")
        print("\n--- MAIN MENU ---")
        print("\n1-Record students")
        print("2-Consult list")
        print("3-Search students")
        print("4-Update information")
        print("5-Delete students")
        print("6-Exit")
        
        option = input("\nEnter an option: ")

        if option == "1":
            clear()
            while True:
                new_student = student_registration()
                record.append(new_student)
                print("\n=================================")
                print("Registration Summary ")
                print("=================================")
                print(F"Name: {new_student['name']}")
                print(f"ID: {new_student['student_id']}")
                print(f"Age: {new_student['age']}")
                print(f"Course: {new_student['course']}")
                print(f"Status: {new_student['student_status']}")
                print("=================================")

                print("\nStudent added successfully")

                add_other = input("\n¿You want to add another student? (yes/no): ")
                clear()

                if add_other == "no":
                    clear()
                    break
                 

        if option == "2":
            clear()
            if not record:
                clear()
                print("NO STUDENTS REGISTERED")
                input("\nPress ENTER to return to the main menu...")
                clear()
            else:
                print("--- CONSULTATION MENU --- ")
                
                for new_student in record:
                    print(f"\nName: {new_student['name']} | ID: {new_student['student_id']} | Age: {new_student['age']} | Course: {new_student['course']} |  Status: {new_student['student_status']}")
                pass

                input("Press ENTER to return to the main menu...")   
                clear()

        if option == "3":
            while True:
                clear()
                print("--- SEARCH MENU ---")
                student_search = input("Enter a name to search: ")
                result = search(record,student_search)

                if result:
                    print("\n=================================")
                    print("Search Summary ")
                    print("=================================")
                    print(F"Name: {result['name']}")
                    print(f"ID: {result['student_id']}")
                    print(f"Age: {result['age']}")
                    print(f"Course: {result['course']}")
                    print(f"Status: {result['student_status']}")
                    print("=================================")

                    other_search = input("\n¿You want to search another student? (yes/no): ")
                    if other_search == "no":
                        clear()
                        break
                else:
                        print(f"THE STUDENT '{student_search}' WAS NO FOUND")
                        input("Press ENTER to return to the main menu...")
                        clear()
                        break
                
        if option == "4":
            clear()
            while True:
                update_information(record)
                input("Press Enter to exit...")
                break

        if option == "5":
            clear()
            while True:
                delete_students(record)
                input("Press Enter to exit...")
                break

        if option == "6":
            print("\nThank you for using the system, goodbye") 
            break     









if __name__ == "__main__":
    main()