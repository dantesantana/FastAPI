"""
Functions
"""


def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


print_my_name("Josh", "Garvey")


def print_color_red():
    color = "Red"
    print(color)


color = "Blue"
print(color)
print_color_red()


def print_numbers(high, low):
    print(high)
    print(low)


print_numbers(low=3, high=10)


def multiply(a, b):
    return a * b


solution = multiply(10, 6)
print(solution)


def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


number_list = [1, 2, 3, 4, 5]  # could also be range(1, 6)
print_list(number_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)


def info_to_dict(firstname, lastname, age):
    return {'firstname': firstname, 'lastname': lastname, 'age': age}


print(info_to_dict('Josh', 'Garvey', 29))
