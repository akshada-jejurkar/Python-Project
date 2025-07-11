# 🔐 Akshada's Password Strength Checker – Core Python

import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[\W_]", password) is None

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        return "🟢 Strong Password"
    elif len(password) >= 6 and not (digit_error or lowercase_error):
        return "🟡 Moderate Password – Add uppercase & symbol"
    else:
        return "🔴 Weak Password – Improve length, mix characters"

def main():
    print("🔐 Welcome to Akshada's Password Strength Checker")
    print("Rules: Minimum 8 characters, mix of uppercase, lowercase, digits, and symbols.\n")

    while True:
        pwd = input("Enter a password to check (or 'exit' to quit): ")

        if pwd.lower() == "exit":
            print("👋 Thanks for using the password checker!")
            break

        result = check_strength(pwd)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
