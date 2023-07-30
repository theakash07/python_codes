number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even=0
odd=0
for i in number:
    if i%2==0:
        even=even+1
    elif i%2!=0:
        odd=odd+1

print(f"The even count is {even}")
print(f"the odd count is {odd}")
