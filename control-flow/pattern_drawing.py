size = int(input("Enter the size of the pattern: "))
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()