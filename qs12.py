import calendar  # Import the calendar module

def main():
    month = int(input("Enter month (1-12): "))  # Prompt the user to enter the month
    year = int(input("Enter year: "))  # Prompt the user to enter the year

    if month < 1 or month > 12:  # Check if the entered month is valid
        print("Invalid month entered.")  # Display an error message
        return  # Terminate the program

    # Call the calendar.month() function to generate the calendar for the specified month and year
    # Print the calendar
    print(calendar.month(year, month))

main()  # Call the main function to start the program execution
