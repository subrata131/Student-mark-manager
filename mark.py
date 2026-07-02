students=[
    {"name":"Rahul ","roll":1,"mark":85}
    {"name":"Subrata","roll":2,"mark":75}
]

max=students[0]["mark"]
low=students[0]["mark"]

while True:
    print("\n===== Student Marks Analyzer =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Highest Marks")
    print("5. Lowest Marks")
    print("6. Average Marks")
    print("7. Exit")

    choice=int(input("Enter your choice:"))
    

    if choice==1:
        name=input("Enter Student name:")
        roll=int(input("Enter Roll number:"))
        mark=int(input("Enter mark:"))
        student={
    "name":name,
    "roll":roll,
    "mark":mark
      }
        students.append(student)

    elif choice==2:
        for student in students:
            print(student)
    elif choice==3:
        roll=int(input("Enter Roll number to search:"))
        for student in students:
            if student["roll"]==roll:
                print(student)
                break
        else:
            print("Student not found.")
    elif choice==4:
        for student in students:
            if student["mark"]>max:
                max=student["mark"]
        print("Student with highest marks:",max)
    elif choice==5:
        for student in students:
            if student["mark"]<low:
                low=student["mark"] 
        print("Student with lowest marks:",low) 
    elif choice==6:
        total=0
        average=0
        for i in students:
            total+=i["mark"]
        average=total/len(students)
        print("Average marks:",average)
    elif choice==7:
        print("Exiting the program.")
        break
        
