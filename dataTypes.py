# List - mutable

marks = [34,5,4,5,34,5,3,5]
print(marks, type(marks))

print(len(marks))
print(marks[0])
print(marks[-1])
print(list(set(marks)))

# slicing a list = list[startingIndex:endingIndex]
print(marks[0:5])
print(marks[-5:])
print(marks[:5])


# Tuple - immutable

marks = (34,5,4,5,34,5,3,5)
print(marks)
print(type(marks))
print(marks[0])
print(marks[-1])
print(marks[0:5])
print(marks[-5:])
print(marks[:5])
print(marks.count(34))
print(marks.index(34))

# Set => unique items in collection
marks = {34,5,4,5,34,5,3,5}
print(marks)
print(type(marks))
print(len(marks))

# Dictionary => key:value pairs

marks = {"Math":94, "Science":59, "Engineering":85}
marks["Science"] = 54
marks["English"] = 98
print(marks.get("Science"))
print(marks["Science"])

