print("Welcome to the Interactive Personal Data Collector!")


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print("Name:", name, "| Type:", type(name), "| Memory Address:", id(name))
print("Age:", age, "| Type:", type(age), "| Memory Address:", id(age))
print("Height:", height, "| Type:", type(height), "| Memory Address:", id(height))
print("Favourite Number:", fav_num, "| Type:", type(fav_num), "| Memory Address:", id(fav_num))

birth_year = 2026 - age

print("\nYour birth year is approximately:", birth_year)

print("\nThank you for using the Personal Data Collector. Goodbye!")