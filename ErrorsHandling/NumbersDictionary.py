numbers_dictionary = {}
line = input()
try:
    while line != "Search":
        first_line=line
        second_line=int(input())
        numbers_dictionary[first_line]=second_line
        line = input()

    line=input()
    while line != "Remove":
        print(numbers_dictionary[line])
        line=input()

    line=input()
    while line != "End":
        numbers_dictionary.pop(line)
        line = input()

except ValueError:
    print("The variable number must be an integer")

except KeyError:
    print("Number does not exist in dictionary")

if len(numbers_dictionary) != 0:
    for key,value in numbers_dictionary.items():
        print(f"{{'{key}': {value}}}")
else:
    print("{}")
