import re

def check_username_validity(username):
    # Ensure the username is between 5 and 15 characters in length.
    if not (5 <= len(username) <= 15):
        return "Invalid username: The username must be between 5 and 15 characters."
    
    # Ensure the username contains only alphanumeric characters and symbols.
    if not re.search(r"[A-Za-z0-9]", username):
        return "Invalid username: The username must contain only alphanumeric characters and symbols."
    
    # Ensure the username starts with a letter.
    if not username[0].isalpha():
        return "Invalid username: The username must start with a letter."
    
    # Ensure the username contains at least one uppercase letter.
    if not re.search(r"[A-Z]", username):
        return "Invalid username: The username must contain at least one uppercase letter."
    
    # Ensure the username contains at least one symbol or special character.
    if not re.search(r"[\W_]", username):
        return "Invalid username: The username must contain at least one symbol."

    return "Valid username."


# Main program that allows users to test the function with their own input
if __name__ == "__main__":
    username = input("Enter a username to check its validity: ")
    result = check_username_validity(username)
    print(result)