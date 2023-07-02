def  main(to):
    print(f"Hello,{to}",end="")#end function by default end next space
    

def mul(num):
    cube=pow(num,3)
    print("The cube is :",cube)


x=int(input("Enter x: "))
y=int(input("Enter y : "))
z=x+y
mul(z)

name=input("Enter you name sir !").strip().title()
main(name)


