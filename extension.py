"""Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java"""
def main():
    file=extension()
    print(f"The file is: .{file} Extension")
    


def extension():
    name=input("Enter file type:")
    #for error handling in code 
    if "." not in name:
       print("Type valid FIle extension:")
    else:
        first,second=name.split(".")
        return second #return the extension name
        
    
    
main()
    
