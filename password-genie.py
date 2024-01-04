import random
import string

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App!")
    
    # Get desired password length from the user
    length = int(input("Enter the desired length of the password: "))
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Your generated password: {password}")

if __name__ == "__main__":
    main()
