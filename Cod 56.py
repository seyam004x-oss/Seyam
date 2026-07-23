char = input("Enter a character: ").lower()

if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")
else:
    print("Please enter a single valid alphabet letter.")
