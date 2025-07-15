import math
def calculate(n):
    root=math.sqrt(n)
    log=math.log(n)
    sine=math.sin(n)
    return root,log,sine

n=int(input("Enter a number: "))
root,log,sine=calculate(n)
print("Square root: ",root)
print("Logarithm: ",log)
print("Sine: ",sine)
