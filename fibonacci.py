# To print fibonacci series

f1 = 0
f2 = 1
f3 = 0

n = int(input("Enter the limit for Fibonacci series: "))
print("The first ", n," numbers in fibonacci series are as follows:")
print(f1)
print(f2)
for i in range(2, n):
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3
