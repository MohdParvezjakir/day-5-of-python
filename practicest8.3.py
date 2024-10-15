#Write a python function to print first n lines of the following pattern:
def pattern(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end="" )
        print()
pattern(3)
