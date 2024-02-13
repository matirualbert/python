class People:
    def __init__(self,name,age,career):
        self.name = name
        self.age = age
        self.career = career
    def show(self):
        print(f"My name is {self.name},"
              f"I'm {self.age} years old "
              f"and I pursue {self.career}.")
person1 = People("Nicholas", 30,"managing director")
person2 = People("Naomi", 20,"interior designer")
person3 = People("Harvey", 25,"lawyer")
person4 = People("Mike Ross", 22,"paralegal")
person5 = People("Albert", 18,"international business man")

person1.show()
person2.show()
person3.show()
person4.show()
person5.show()
