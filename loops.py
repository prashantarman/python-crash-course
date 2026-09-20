# range
num = range(5)
print(num)
# range needs 3 values start, stop, step. start and step is by default 0 and 1, but we need to pass stop everytime range(start, stop, step)

# counter 1 to 5
i = 1
while i <= 5:
    # whenever an integer number gets multiplied by a string then string gets repeated
    print(i * "next number")
    i += 1

# counter 5 to 1
i = 5
while i > 0:
    print(i * "*")
    i -= 1

# for loops

num = range(5)

for i in num:
    print(i)

for i in range(1, 6):
    print(i)


# check even number
for i in range(11):
    if i%2==0:
        print(i)
for i in range(2, 11, 2):
    print(i)

# break and continue

# print multiple of 3 in [1 to 50] and stops at 21
for i in range(51):
    if i == 21: continue
    if i%3==0:
        print(i)