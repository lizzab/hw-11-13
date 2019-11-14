# Ben Lizza
# 11/13/19
# I am making a Class for a person that will be used in Commands.py


class Person:
    def __init__(self, first_name, middle_int, last_name, age, sex, weight):
        self.first_name = first_name
        self.middle_int = middle_int
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.weight = weight

    def name(self):
        "This persons name is " + self.first_name + self.middle_int + self.last_name, "and is a" + self.sex
        "He is " + self.age, "and weighs" + self.weight
        return

    def birthday(self):
        int(self.age) + 1
        "It's this persons birthday! They are now " + str(self.age)
        return




