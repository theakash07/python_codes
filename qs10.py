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

#one more approach to the question 

def main():
    num=input("Enter data: ")
    sum=getdata(num)
    
def getdata(n):
    n1=n+n
    n2=n+n+n
    
    print(int(n)+int(n1)+int(n2))
    
main()
