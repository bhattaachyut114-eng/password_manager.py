# Password Manager

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, secure command-line password manager for storing and managing account credentials.

**Repository:** [https://github.com/bhattaachyut114-eng/password_manager.py](https://github.com/bhattaachyut114-eng/password_manager.py)

## Features

- **Master Password Protection**: Authenticate with a master password before accessing stored passwords
- **Hidden Input**: Uses `getpass` to hide password input from the terminal
- **Clean Menu Interface**: Simple and intuitive command-line interface
- **Password Storage**: Stores credentials locally in `passwords.txt`
- **Input Validation**: Prevents empty account names or passwords

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhattaachyut114-eng/password_manager.py.git
cd password_manager.py
```

2. Run the password manager:
```bash
python password_manager.py
```

### Requirements

- Python 3.6 or higher
- No external dependencies required

### First Launch

Enter the master password when prompted:
```
Master password: ________
```

Default master password is `achyut123`. Change this in the code for production use.

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
- `passwords.txt` - Stores account credentials (auto-created, gitignored)
- `README.md` - This documentation
- `LICENSE` - MIT License
- `.gitignore` - Git ignore rules

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

⚠️ **Important**: This is a basic password manager for learning and personal use. It stores passwords in plain text locally.

**For Production Use:**
1. Change the hardcoded `MASTER_PASSWORD` in the code to a strong password
2. Consider using encryption (e.g., `cryptography` library) for stored passwords
3. Never commit `passwords.txt` to version control (already excluded via `.gitignore`)
4. Use this only on trusted, secure systems

**Security Features:**
- Hidden password input (asterisks displayed)
- Master password authentication
- Input validation
- UTF-8 encoding support

## Example Workflow

```
Master password: achyut123
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
