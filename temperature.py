#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

temp=int(input("Enter Temp: "))
choice=int(input("Enter 0 for celsius conversion and 1 for farenheit: "))

match choice:
    case 0:
        print("celsius to farehnheit Conversin: ")
        farenheit=((9/5)*(temp+32))
        print(f"The farenheit is:-  {farenheit}")
    case 1:
        print("COnversion of farenheit to celsius : ")
        celsius=((temp-32)*(5/9))
        print(f"The celsius is :- {celsius} ")


    

