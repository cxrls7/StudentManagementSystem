from src.funtions import student_registration, clear

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
        
        option = input("Enter an option: ")

        if option == "1":
            clear()
            while True:
                new_student = student_registration()
                record.append(new_student)

                print("\nStudent added successfully")

                add_other = input("\nYou want to add other student (yes/no): ")

                if add_other == "no":
                    clear()
                    break



if __name__ == "__main__":
    main()