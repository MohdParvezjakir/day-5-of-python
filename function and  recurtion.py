# a function is a group of statement that perform a specific task 
# syntax of a function 
def funcname(): # function defination 
    print("hello")
funcname()# funtion call
def greet():# program for greet a user
    name=input("Enter your name:")
    print(f"hello, {name}")
    return 

#function with argument
def greet2(name, ending):
    print("hello" + name  + ending)
    return

# function with predefined argument
def greet2(name="parvez", ending="bye"):
    print("hello"  +name +    ending)
    return
greet2("faijan", "thank you")

        
   




