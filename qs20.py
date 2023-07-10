def getdata(name, n):
    result = ""
    for _ in range(n):
        result += name + " "
    return result

print(getdata("hello", 2))
print(getdata(".Akash", 3))
