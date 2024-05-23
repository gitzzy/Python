class Student:
    def setData(self):
        self.id = int(input("Enter Your ID : "))
        self.name = input("Enter Your Name : ")

    def getData(self):
        print("ID : ",self.id)
        print("Name : ",self.name)

obj = Student()
obj.setData()
obj.getData()