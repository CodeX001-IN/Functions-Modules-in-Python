#defining the factorial function
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1) 
#main program 
if __name__== "__main__":
    a=int(input("Enter a number: "))
    print(f"faactorial of {a} is: " ,factorial(a))
