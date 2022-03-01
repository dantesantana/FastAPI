"""
Flow Control: If Else ElIf
"""

x = 0
# 4 space indentation indicates code is inside a block
# i.e. the first print here is considered inside the if statement
if x > 1:
    print("x greater than 1")
else:
    print("x is not greater than 1")
print("Outside of if statement")

hour = 21
if hour < 15:
    print("Good morning!")
elif hour < 20:
    print("Good afternoon!")
else:
    print("Good night!")


grade = 63

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")