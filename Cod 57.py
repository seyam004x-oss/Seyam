char = input("Enter an alphabet: ")

if char.isupper():
    print(f"'{char}' is Uppercase.")
elif char.islower():
    print(f"'{char}' is Lowercase.")
else:
    print("It is not a letter.")
