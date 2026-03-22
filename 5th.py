student={}
def add():
    name=input("Enter your name:")
    mark=int(input("Enter your mark:"))
    student[name]=mark
    save()
    print("Student added")

def show():
    if len(student)==0:
        print("No data")
        return
    for o,i in student.items():
        print(o,":",i)

def high():
    if len(student)==0:
        print("No data")
        return
    maxi=max(student.values())

    for o,i in student.items():
     if(i==maxi):
        print("Topper:",o,"mark:",i)

def save():
    with open("mark.txt","w") as f:
        for o,i in student.items():
            f.write(o + "," + str(i) + "\n")

def load():
    try:
        with open("mark.txt","r") as f:
            for line in f:
                name, marks =line.strip().split(",")
                student[name]=int(marks)
    except:
        pass

def delete():
    n=input("Enter name to delete:")
    if n in student:
        del student[n]
        save()
        print("Delete successfully")
    else:
        print("Student not found")

def update():
    n=input("Enter name:")
    if n in student:
        new=int(input("Enter New mark:"))
        student[n]=new
        save()
        print("Update successfully")
    else:
        print("Student not found")

def search():
    n=input("Enter name:")
    if n in student:
        print(n,":",student[n])
    else:
        print("Student not found")


load()
while True:
    print("\n1.Add\n2.Show\n3.Topper\n4.Delete\n5.Update\n6.Search\n7.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add()
    elif ch == 2:
        show()
    elif ch == 3:
        high()
    elif ch == 4:
        delete()
    elif ch==5:
        update()
    elif ch==6:
        search()
    elif ch==7:
        break
    else:
        print("Invalid")

