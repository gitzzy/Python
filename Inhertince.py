class Netflix:
    def __init__(self,id,plan,duration):
        self.id = id
        self.plan = plan
        self.duration = duration

    def Suscribe(self):
        print(f"Account with ID : {self.id} has Suscribed to {self.plan} Plan for {self.duration} Months.")

    def UnSuscribe(self):
        print(f"Account with ID : {self.id} has Unsuscribed to {self.plan} Plan.")

obj = Netflix(2134456,"Premium",4)
obj.Suscribe()

class Screens(Netflix):

    def __init__(self, id, plan, duration, Screen):
        super().__init__(id, plan, duration)
        self.Scrin = Screen

    def Update(self):
        print(f"{self.id} has Added {self.Scrin} Extra Screen in {self.plan} Plan.")

obj1 = Screens(2134456,"Premium",4,2)
obj1.Update()


