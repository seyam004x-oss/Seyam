a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Triangle inequality theorem: sum of any two sides must be greater than the third
if (a + b > c) and (a + c > b) and (b + c > a):
    print("A valid triangle can be formed.")
else:
    print("A valid triangle cannot be formed.")
