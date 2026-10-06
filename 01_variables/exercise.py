# Exercise 1: Variables and data types
#
# Read lesson.md first if you haven't yet.
# Complete each TODO. Run this file with:
#   python 01_variables/exercise.py

# TODO 1: Create a variable "my_name" with your name (text)
my_name = 'Jaime de Pablos'

# TODO 2: Create a variable "my_age" with your age (whole number)
my_age = 30

# TODO 3: Create a variable "height" with your height in meters (decimal number), e.g. 1.75
height = 1.80

# TODO 4: Print a sentence using an f-string that combines the three variables above
# Expected example output: "My name is Jaime, I'm 30 years old and I'm 1.80 meters tall"
print(f"Mi nombre es {my_name}, tengo {my_age} años y mido {height} metros de altura")

# TODO 5: Ask the user for their name with input() and store it in a variable "user_name"
user_name = input("¿Cuál es tu nombre? ")
print(f"Hola {user_name}, ¡mucho gusto!")

# TODO 6: Ask the user for a number with input(), convert it to int, and store it in "user_number"
user_number = int(input("Escribe un número: "))    
print(f"El número que escribiste es {user_number}")

# TODO 7: Print double the value of "user_number"
# Example: if the user types 5, it should print 10
print(f"El doble de {user_number} es {user_number * 2}")