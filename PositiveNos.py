# Python program to print all positive numbers in a range

N = 0
input_list = []

N = int(input("Enter the range for integers: "))
print("Enter the integers:")
for i in range(N):
     n = int(input())
     input_list.append(n)

print("The positive integers in the given range are:")
for j in range(N):
    if input_list[j] > 0:
        print(input_list[j])
