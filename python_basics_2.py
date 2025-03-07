
# Python Functions

def add(num1, num2):
    return num1 + num2

print(add(3, 4))
sum = add(3,4)
print(sum)
print(add(12, 2332))
print(add(2123, 233223))


#Lists and Loops
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

list_length = len(fruits)
print("the length of the fruits array is = ", list_length)
# len(name of the list) this gives you the length of the list

for i in fruits:
    # fruit 1 = apple
    # fruit 2 = banana
    # fruit 3 = cherry

    print('fruit = ', i)

    # Dictonary
person1 = {"name": "John", "age": 25, "employed": True, "marks": [90, 80, 70]}
print(person1)
print(person1["name"])
print(person1["age"])
print(person1["employed"])
print(person1["marks"])
print(person1["marks"][0])
print(person1["marks"][1])
print(person1["marks"][2])

# key - vaue pairs
# key = name, value = John