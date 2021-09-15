def factorial(n):
    prod = 1
    for i in range(n,1,-1):
        prod = prod*i
    return prod

def fib(n):
    if(n<2):
        return n
    else:
        return fib(n-1)+fib(n-2)


#main
print("Good News Everyone!")
print(f"5! = {factorial(5)}" )
print(f"fib(5) = {fib(5)}" )
