print("hello world", "checks")

name = "Prashant"

# f-string (modern, most readable)
print(f"Hello {name}. How are you?")

# Old way with .format()
print("Hello {}. How are you?" .format(name))

# Even older way with % formatting
print("Hello %s. How are you?" %name)

# get data type
print(type(name))


# Take input from user
name = input("Enter your name: ")
print("Hello "+name)

#  Practice 1
fName = "Tony"
lName = "Stark"
age = 58
height = 1.85

superHero = input("What is your favorite hero name? ")
print(fName+" is secretly a "+superHero)