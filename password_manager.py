import os
import sys
import getpass
import platform

PASSWORD_FILE = "passwords.txt"
MASTER_PASSWORD = "secure123"


def get_masked_password(prompt="Password: "):
    """Get password input with asterisks displayed for each character."""
    if platform.system() == "Windows":
        import msvcrt
        password = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        
        while True:
            char = msvcrt.getch()
            if char in (b'\r', b'\n'):
                print()
                break
            elif char == b'\x08':  # Backspace
                if password:
                    password = password[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                try:
                    password += char.decode('utf-8')
                    sys.stdout.write('*')
                    sys.stdout.flush()
                except:
                    pass
        
        return password
    else:
        # Fallback for non-Windows systems
        return getpass.getpass(prompt)


def ensure_password_file():
    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "w", encoding="utf-8"):
            pass


def load_passwords():
    passwords = []
    with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or "|" not in line:
                continue
            account, pwd = line.split("|", 1)
            passwords.append((account.strip(), pwd.strip()))
    return passwords


def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("No saved passwords found.")
        return

    print("\nSaved passwords:")
    for account, pwd in passwords:
        print(f"- {account}: {pwd}")
    print()


def add_password():
    account = input("Account name: ").strip()
    if not account:
        print("Account name cannot be empty.")
        return

    password = get_masked_password("Password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
        file.write(f"{account}|{password}\n")
    print("Password saved.")


def authenticate():
    entry = get_masked_password("Master password: ")
    return entry == MASTER_PASSWORD


def main():
    ensure_password_file()

    if not authenticate():
        print("Authentication failed.")
        return

    while True:
        print("\nOptions: [view] Show passwords  [add] Save password  [quit] Exit")
        choice = input("Select an option: ").strip().lower()

        if choice == "view":
            view_passwords()
        elif choice == "add":
            add_password()
        elif choice == "quit":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose view, add, or quit.")


if __name__ == "__main__":
    main()
