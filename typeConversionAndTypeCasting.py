age = input("Enter your age: ")
print("Your age is "+age, type(age))
# output
# Your age is 45 <class 'str'>

# if we add 1 in age it will throw error TypeError: can only concatenate str (not "int") to str
# print(age+1)
# to fix this we will do typecasting that is conversion done by user
new_age = int(age)+1
print(new_age)

# type conversion that is automatically done by python interpreter
print(1+7.5)