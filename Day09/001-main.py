programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

empty_dictionary = {}

empty_dictionary["bug"] = "nobug"


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])