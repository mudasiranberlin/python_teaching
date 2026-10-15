class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

student1 = Student("Ali", 20)

student1.introduce()

print("Here is The Everthing",student1)