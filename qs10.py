def main():
    num = take_num()
    final_result = value(num)
    print("The value is:", final_result)

def take_num():
    data = input("Enter Number: ")
    return int(data)

def value(n):
    nn = int(str(n) + str(n))  # Concatenate n with itself
    nnn = int(str(n) + str(n) + str(n))  # Concatenate n with itself twice
    result = n + nn + nnn
    return result

main()
