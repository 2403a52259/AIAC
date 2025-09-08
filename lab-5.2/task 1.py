import hashlib

users_db = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register():
    username = input("Enter a new username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in users_db:
        print("Username already exists.")
        return
    password = input("Enter a new password: ").strip()
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    users_db[username] = hash_password(password)
    print("Registration successful.")

def login():
    username = input("Enter your username: ").strip()
    if username not in users_db:
        print("Username does not exist.")
        return
    password = input("Enter your password: ").strip()
    if users_db[username] == hash_password(password):
        print("Login successful.")
    else:
        print("Incorrect password.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "main":
    main()
