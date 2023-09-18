#def menu to select what to pick
def getgrades():
    grades = []
    while len(grades)<3:
        grade=input("Please enter the students assessment grade: ")
        try:
            grade=float(grade) #Convert input number from string to float
            if grade < 0 or grade > 100:
                print("Error! The number must be between 1 and 100")
            else:
                grades.append(grade)
        except ValueError:
            print("Error! please input a valid number")
    return grades

def main():
    gradebook={}
    while True:
        name = input("Please enter the students name or type quit to quit: ")
        if name == 'quit':
            break
        grades = getgrades()
        gradebook[name] = grades
    
    print("\nGradebook Summary:")
    for student, grades in gradebook.items():
        # Calculate the average grade for the current student
        average = sum(grades) / len(grades)
        # Display the student's name and average grade to the console
        print(f"\nStudent: {student}")
        print(f"Average Grade: {average}")

# Call the main function to run the program
main()

    
