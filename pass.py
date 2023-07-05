def main():
    x=get_int("what X:?")
    print(f"x is {x}")
    
    
def get_int(prompt):#passing parameter prompt to make code more dynaminc 
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
        
main()
