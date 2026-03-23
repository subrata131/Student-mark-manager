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
    print("\n...Student list...")
    print("--------------------")
    for o,i in student.items():
        print(f"{o:<10} | {i}")
    print("-------------------")

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
        print("Deleted successfully")
    else:
        print("Student not found")

def update():
    n=input("Enter name:")
    if n in student:
        new=int(input("Enter New mark:"))
        student[n]=new
        save()
        print("Updated successfully")
    else:
        print("Student not found")

def search():
    n=input("Enter name:")
    if n in student:
        print(n,":",student[n])
    else:
        print("Student not found")

def sort():
    if len(student)==0:
        print("No data")
        return
    s=sorted(student.items(),key=lambda x:x[1],reverse=True)
    print("\n....Sorted Student...")
    for o,i in s:
        print(f"{o}:{i}")

def top3():
    if len(student)==0:
        print("No data")
        return
    s=sorted(student.items(),key=lambda x:x[1],reverse=True)
    print("\n...Top 3 students...")
    for i in range(min(3,len(s))):
        name,marks=s[i]
        print(f"{i+1}.{name}:{marks}")



load()
while True:
    print("\n1.Add\n2.Show\n3.Topper\n4.Delete\n5.Update\n6.Search\n7.Sort\n8.Top 3\n9.Exit")

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
        sort()
    elif ch==8:
        top3()

    elif ch==9:
        print("Exiting....")
        break
    else:
        print("Invalid")

