def main():
    m = month()  # Prompt the user to enter the month for the first set of details
    y = year()  # Prompt the user to enter the year for the first set of details
    d = date()  # Prompt the user to enter the date for the first set of details
    print("Second details please:")
    m1 = month()  # Prompt the user to enter the month for the second set of details
    y1 = year()  # Prompt the user to enter the year for the second set of details
    d1 = date()  # Prompt the user to enter the date for the second set of details

    # Check for invalid month values
    if m > 12 or m1 > 12:
        print("Invalid Month")
        return

    # Check for invalid date values
    if d > 31 or d1 > 31:
        print("Invalid Date")
        return

    # Calculate the difference in years
    if y == y1:
        yr = 0
    else:
        yr = abs(y - y1)

    # Calculate the difference in months
    if m == m1:
        mn = 0
    else:
        mn = abs(m - m1)

    # Calculate the difference in days
    if d == d1:
        dt = 0
    else:
        dt = abs(d - d1)

    print(f"The gap between years {yr}-{mn}-{dt}")  # Print the calculated difference


def month():
    return int(input("Enter month (1-12): "))  # Prompt the user to enter a month


def year():
    return int(input("Enter year: "))  # Prompt the user to enter a year


def date():
    return int(input("Enter date (1-31): "))  # Prompt the user to enter a date


main()  # Call the main function to start the program execution
