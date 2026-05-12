# Password Manager

A simple, secure command-line password manager for storing and managing account credentials.

## Features

- **Master Password Protection**: Authenticate with a master password before accessing stored passwords
- **Hidden Input**: Uses `getpass` to hide password input from the terminal
- **Clean Menu Interface**: Simple and intuitive command-line interface
- **Password Storage**: Stores credentials locally in `passwords.txt`
- **Input Validation**: Prevents empty account names or passwords

## How to Use

### Running the Tool

```bash
python password_manager.py
```

### First Launch

Enter the master password when prompted:
```
Master password: ________
```

Default master password is `secure123`. Change this in the code for production use.

### Menu Options

Once authenticated, you'll see the menu:

```
Options: [view] Show passwords  [add] Save password  [quit] Exit
Select an option:
```

#### View Passwords
- Type `view` to display all saved passwords
- Shows account names and corresponding passwords

#### Add Password
- Type `add` to save a new password
- Enter the account name (e.g., "Gmail", "GitHub")
- Enter the password (input is hidden)

#### Quit
- Type `quit` to exit the program

## File Structure

- `password_manager.py` - Main application
- `passwords.txt` - Stores account credentials (auto-created)
- `README.md` - This documentation

## Security Notes

⚠️ **Important**: This is a basic password manager for learning/personal use. For production use:

1. Change the hardcoded `MASTER_PASSWORD` to a strong password
2. Consider using encryption (e.g., `cryptography` library)
3. Never commit `passwords.txt` to version control
4. Add the file to `.gitignore`

## Example Workflow

```
Master password: secure123
Authentication successful!

Options: [view] Show passwords  [add] Save password  [quit] Exit
Select an option: add
Account name: Gmail
Password: ________
Password saved.

Options: [view] Show passwords  [add] Save password  [quit] Exit
Select an option: view

Saved passwords:
- Gmail: my_secure_password

Options: [view] Show passwords  [add] Save password  [quit] Exit
Select an option: quit
Goodbye.
```
