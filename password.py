import random

print("Random Password Generator")
print("--------------------------")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        print("Choose what to include in your password:")
        print("1. Letters only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Symbols")

        choice = input("Enter your choice (1/2/3): ")

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()_-+=<>?/{}[]|~"

        if choice == "1":
            chars = letters
        elif choice == "2":
            chars = letters + numbers
        elif choice == "3":
            chars = letters + numbers + symbols
        else:
            print("Invalid choice, using letters only by default.")
            chars = letters

        password = ""
        for i in range(length):
            password += random.choice(chars)

        print("\nYour random password is:", password)

except:
    print("Something went wrong, please try again.")
