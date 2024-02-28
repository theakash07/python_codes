# Title: 

# Prompt the user to enter a string
ch = input("Enter string")

# Iterate through each character in the input string
for i in ch:
    # Check if the character is an uppercase letter
    if "A" <= i <= "Z":
        # Print a message indicating that the character is uppercase
        print("The %s is upper" % i)
    else:
        # Print a message indicating that the character is lowercase
        print("The %s is lower" % i)
