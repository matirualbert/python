class Fruits:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def onyesha(self):
        print(f"My favourite Fruit is {self.name}"
              f" and it costs Ksh.{self.price}"
              f" and its {self.color} in color.")
myobj=Fruits("Banana",200,"yellow")
myobj2=Fruits("Grapes",500,"maroon")
myobj.onyesha()
myobj2.onyesha()