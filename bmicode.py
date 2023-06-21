weight=int(input("Enter your wight: "))
height=int(input("Enter you height in Cm"))

ht=height/100
bmi=weight/(ht**2)

print("Your BMI index : \n",bmi)
if bmi<18:
    print("You are underweight")
elif bmi<24:
    print("You are normal")
elif bmi>24:
    print("You are overweight")
