                                                   #variables
Favourite_Number = 9
print(f"my fav no. is {Favourite_Number}")

greeting = "Hello plp"
print(greeting)

is_python_fun = True
is_python_boring = False
print(f"Is python fun? {is_python_fun}")
print(f"Is python boring? {is_python_boring}")

                                               #control flow if, elif, else
feast = 100
if feast > 90:
    print("the meal is delicious")
elif feast >= 50:
    print("the meal is good")
else:
    print("the meal is nice ")

                                            #loops for, while
for i in range(9):
    print(f"the door bell rings twice {i}")

CountDown = 4
while CountDown > 0:
    print(f"the countdown is: {CountDown}")
    CountDown -= 1
print("take off!")

                                              #function
def greet(someone):
    return F"good evening, {someone}!"
#apply the function
print(greet("Ian"))
print(greet("Mugo"))

                                                #lists
fruits_list = ["apple", "mango", "banana", "melon"]
fruits_tuple = ("cherry", "pears", "plums", "avocado")
print(fruits_list)
print(fruits_tuple)

                                                #dictionaries
Contacts = {
    "ian": "748674752",
    "mugo": "878/8796",
    "chakin": "98757424"
}
print(f"this is the contact for ian {Contacts["ian"]}")

                                                #module
#inbuilt module
import math 
result = math.sqrt(69)
print(f"the answer is, {result}")

#custom module
import someone_module
print(someone_module.greet("ian"))