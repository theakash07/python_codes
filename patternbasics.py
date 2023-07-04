def main():
    print_block(5)
    
    
    
def print_block(size):
    #for column
    for i in range(size):
        print("#",end=" ")
        #for row
        for j in range(size):
            print("#",end=" ")
        print()


main()
