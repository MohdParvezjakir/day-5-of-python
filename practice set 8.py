#write a program  to find the greatest number with the help of function 
def greatestnumber():
    a= int(input("Enter your nuumber(a):"))
    b= int(input("Enter your nuumber(b):"))
    c= int(input("Enter your nuumber(c):"))
    if (a>b and a>c):
        print(f"greatest number is {a}")
    elif (b>a and b>c):
        print(f"greatest number is {b}")
    elif (c>b and c>a):
        print(f"greatest number is {c}")
    elif (a==b==c):
        print("all number is equal")
    print(f"Average of your number is,({a + b + c /9}) :")
    
    return
greatestnumber()

