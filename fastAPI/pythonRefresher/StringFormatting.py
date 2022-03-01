"""
String Formatting
"""
first_name="Eric"
# normal print statement
print("Hi "+first_name)
# f string formatting
print(f"Hi {first_name}")
# pass in variables
sentence = "Hi {} {}"
last_name="Roby"
print(sentence.format(first_name,last_name))

print(f"Hi {first_name} {last_name}, I hope you are learning.")