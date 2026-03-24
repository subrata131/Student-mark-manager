class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    def show(self):
        print(self.name, self.__mark)
    
    def get(self):
       return self.__mark
    
    def set_mark(self,mark):
       if mark>=0:
          self.__mark=mark
       else:
          print("Invalid mark")


# def load(self):
#     try:
#         with open("mark.txt","r") as f:
#             for line in f:
#                 name,mark =line.strip().split(",")
#                 s=Student(name,int(mark))
#                 self.students.append(s)
#     except:
#         pass

# class manager:
#     def __init__(self):
#         self.students=[]



# students = []  
# load()
class manager:
    def __init__(self):
        self.students=[]
        self.load()

    def add(self):
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))

        s = Student(name, mark)
        self.students.append(s)
        self.save()

        print("Student added")


    def show(self):
       if len(self.students) == 0:
        print("No data")
        return

       for s in self.students:
           s.show()


    def top(self):
      if len(self.students) == 0:
        print("No data")
        return

      topper = max(self.students, key=lambda x: x.get())
      print("Topper:", topper.name, topper.get())


    def search(self):
      name = input("Enter name: ")

      for s in self.students:
        if s.name == name:
            print("Found:", s.name, s.get())
            return  

      print("Student not found")

    def save(self):
      with open("mark.txt","w") as f:
        for i in self.students:
            f.write(i.name + "," + str(i.get())+"\n")

    def load(self):
       try:
          with open("mark.txt","r") as f:
            for line in f:
                name,mark =line.strip().split(",")
                s=Student(name,int(mark))
                self.students.append(s)
       except:
          pass



m=manager()

while True:
    print("\n1.Add\n2.Show\n3.Topper\n4.Search\n5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        m.add()
    elif ch == 2:
        m.show()
    elif ch == 3:
        m.top()
    elif ch == 4:
        m.search()
    elif ch == 5:
        break
    else:
        print("Invalid Input")
     
        