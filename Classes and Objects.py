class Robot:
    #This is a constructor
    def __init__(self,name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self): #add self to every method in class
        print("My name is " + self.name)
#r1 = Robot()
#r1.name = "Tom"
#r1.color = "red"
#r1.weight = 30
#r1.introduce_self()

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduce_self()
r2.introduce_self()
#ctrl + k = committ
#ctrl + alt + k = push
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky","talkitive", True)
p1.robot_owned = r2
p2.robot_owned = r1
p1.robot_owned.introduce_self()
