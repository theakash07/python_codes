#sortest program to find a numeb is even or odd
#program 1:
print("Even") if int(input("Enter number"))%2==0 else print("Odd")

#program 2:
# This is a Python script that determines if a user-inputted number is even or odd.

# Function Definition
k = lambda a: "Even" if int(input("Enter Number")) % 2 == 0 else "Odd" 
# The function `k` is a lambda function that takes one argument `a`. 
# However, the argument `a` is not used in the function. 
# Instead, the function prompts the user to input a number. 
# It checks if the number is even by using the modulus operator `%` with 2. 
# If the number is even (i.e., the remainder of the division by 2 is 0), it returns the string "Even". 
# Otherwise, it returns the string "Odd".

# Function Call
print(k(14))
# The function `k` is called with the argument `14`. 
# However, the argument `14` is not used in the function. 
# The function will still prompt the user to input a number. 
# The result (either "Even" or "Odd") is then printed.


#program 3:
l=["even" if int(input("Enter x"))%2==0 else "false"] #list comprehension
print(l)

