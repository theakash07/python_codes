"""Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers."""

#approach 1
elements = input('Enter numbers: ')#taking strings with comma seprated
numbers = elements.split(",")
tuple_numbers = tuple(numbers)

print(numbers)
print(tuple_numbers)




#approach 2
elements = input('Enter numbers: ')
numbers = [int(num) for num in elements.split(",")]
tuple_numbers = tuple(numbers)

print(numbers)
print(tuple_numbers)
