def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter a number:\t"))
print("Factorial of",n,"is",fact(n))