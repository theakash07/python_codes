filename=input("Enter file Name with extension:")
first,last=filename.split(".")

print(first)
print(last)

match last:
    case "c":
        print("C file")
    case "java":
        print("java file")
    case "gif":
        print("image file")
    case "jpeg":
        print(" image file")
    case _:
        print("i dont have information")

        
