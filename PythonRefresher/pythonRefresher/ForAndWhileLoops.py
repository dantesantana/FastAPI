"""
For & While Loops
"""
my_list = [1, 2, 3, 4, 5]

# print(my_list[0:4])

sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x
print(sum_of_for_loop)


i = 0
while i < 5:
    i += 1
    # skip when i is 3
    if i == 3:
        continue
    print(i)
    # halt execution when i is 4
    if i == 4:
        break
# else executes the first time the while loop fails
else:
    print("i is now larger than or equal to 5")

"""
Given my_list
- create a while loop that prints all elements 3 times
- when priniting elements, use a for loop
- skip Mondays
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i = 0
while i < 3:
    i += 1
    for j in my_list:
        if j == "Monday":
            print("-----")
            continue
        print(j)
