import re

def check_password_strength(password):
    """
    Check the strength of a password based on multiple criteria.

    Args:
        password (str): The password to evaluate.

    Returns:
        tuple: A string indicating the password strength and a list of feedback messages.
    """
    feedback = []

    # Criteria Checks
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    if not any(char.islower() for char in password):
        feedback.append("Password must contain at least one lowercase letter.")
    if not any(char.isupper() for char in password):
        feedback.append("Password must contain at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        feedback.append("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password must contain at least one special character (!@#$%^&* etc.).")

    # Determine Strength
    if len(feedback) == 0:
        strength = "Strong"
    elif len(feedback) <= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

# Get password input from the user
password = input("Enter your password to check its strength: ").strip()

# Check the password strength
strength, feedback = check_password_strength(password)

# Display the result
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
