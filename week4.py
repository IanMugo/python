class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Prompt the user to input their details
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

# Convert age to an integer
try:
    age = int(age)
except ValueError:
    print("Invalid input for age. Setting age to 0.")
    age = 0

# Create an instance of the Person class with user-provided details
person_instance = Person(name=name, age=age, gender=gender)

# Call the introduce method
person_instance.introduce()
