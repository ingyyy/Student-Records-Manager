student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": [],
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name ,grade):
    if name in student_records:
        student_records[name]["grades"].append(grade)
        print(f"Grade {grade} added for student '{name}'.")        
    else :
        print(f"Student '{name}' not found.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return 0.0
    
    grades = student_records[name]["grades"]
    if not grades: 
        return 0.0
    return sum(grades) / len(grades)

def list_students_by_course(course):
    lst = []
    for name, data in student_records.items():
        if course in data["courses"]:
            lst.append(name)
    return lst

def filter_top_students(percentage):
    lstt = []
    for i in student_records:
        m = calculate_average_grade(i)
        if m > percentage:
            lstt.append(i)
    return lstt

def main():
    while True:
        print("*"*35)
        print("Student Records Manager")
        print("*"*35)
        print("Choose your input ")
        print("1. Add a new student")
        print("2. Add grade to a student")
        print("3. Check course enrollment")
        print("4. Calculate student average grade")
        print("5. List students by course")
        print("6. Filter top-performing students")
        print("7. Exit")
        print("=" * 35)
        choice = (input()) 
#choosing
        if choice == '1':
            name = str(input("Enter student's name "))
            while True:
                try : 
                  age = int(input("Enter student's age "))
                  break
                except ValueError:
                   print("Please Enter a valid age")
            coursee = str(input("Enter student's course "))
            add_student(name, age, [coursee])
            print("--> Choose your next option")
            print(" ")
        elif choice == '2' :
            name = str(input("Enter student's name "))
            while True:
                try : 
                   g = float(input("Enter student's grade "))
                   add_grade(name,g)
                   break
                except ValueError:
                    print("Wrong type, please enter a valid grade. ")
            print("--> Choose your next option")
            print(" ")
        elif choice == '3':
            name = str(input("Enter student's name "))
            coursee = str(input("Enter student's course "))
            print( is_enrolled(name,coursee))
            print("--> Choose your next option")
            print(" ")
        elif choice =='4':
            name = str(input("Enter student's name "))
            print(calculate_average_grade(name))
            print("--> Choose your next option")
            print(" ")
        elif choice == '5' :
            coursee = str(input("Enter student's course "))
            print(list_students_by_course(coursee))
            print("--> Choose your next option")
            print(" ")
        elif choice =='6' :
            while True:
                try : 
                   g = float(input("Enter percentage of TOP STUDENTS"))
                   break
                except ValueError:
                    print("Please Enter a valid grade")
            print(filter_top_students(g))
            print("-->  Choose your next option")
            print(" ")
        elif choice == '7':
            print("Bye ")
            break
        else:
            print('Please choose a number between 1 to 7 :  ')
main()
