# lambda functions in python
# a function without a  name is anonymous function or lambda function
# used when we need a small function for a short period of time

# syntax: lambda arguments: expression

def add(x, y):
    return x + y

print(add(2, 5)) # output: 7

# using lamda function
add_lamda = lambda x, y: x+y
print(add_lamda(4,2))

square = lambda x: x**2
print(f"Square of 8 is {square(8)}")


print("---lambda function with map(),filter and sorted -----")

print("--using indexing--")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# from using index
for i, num in enumerate(numbers): # enumerate() function adds a counter to each item ie i is counter, number is item
    print(f"Index: {i}, Number: {num}")

# iterating dictionary
student = {"name": "Hari", "age":25}
for key, value in student.items(): # items() are used with dictionaries which gives key and value together.
    print(f"Key: {key}, Value: {value}")


print("---sorting--")
# sorted() function : used to sort the elements of a list in ascending or descending order
numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers)) # sorting in ascending order
print(sorted(numbers, reverse=True)) # sorting in descending order

# sort by key
students = [("Brick", 50), ("Jane", 25), ("Veronica", 22)]
sorted_students = sorted(students, key=lambda x: x[1]) # sorting by age
print(sorted_students)


print("------filter() function------")
# filter () function : used to filter elements based on a condition
# syntax: filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6]

even_numbers= filter(lambda x: x % 2 == 0, numbers) # filtering even numbers
print(list(even_numbers))

# without lambda function
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# filter people who is 18+
peoples = [{"name":"Joe", "age":20}
            ,{"name":"Oxford", "age":15}
            ,{"name":"Den", "age":22}]

legal_people = filter(lambda x:x["age"]>=18,peoples)
print(f"Legal People: {list(legal_people)}")



print("------map() function------")
# map() function : used to apply a function to all the elements of an iterable
# syntax: map(function, iterable)
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x:x**2, numbers)) # squaring each number in the list
print(squared_numbers)

# multiple iterables
num1 = [1, 2, 3]
num2 = [4, 5, 6]
result = list(map(lambda x,y: x+y, num1,num2)) # adding corresponding elements of two lists
print(result)

# convert to uppercase
names = ["lamda", "function", "uppercase"]
upper_names = list(map(lambda x:x.upper(),names)) # converting each name to uppercase
print(upper_names)


# lambda with multiple conditions
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4)) 

# lambda returning multiple values
calculate = lambda x:(x, x**2, x**3)
print(calculate(5))

# nested lambda function
nested_lamda = lambda x: (lambda y: x +y)
print(nested_lamda(5)(3))