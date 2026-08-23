import string
import getpass


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters.")
    else:
        feedback.append("Use at least 8 characters.")

    checks = [
        (any(c.isupper() for c in password), "Add an uppercase letter."),
        (any(c.islower() for c in password), "Add a lowercase letter."),
        (any(c.isdigit() for c in password), "Add a number."),
        (any(c in string.punctuation for c in password), "Add a special character."),
    ]

    for passed, message in checks:
        if passed:
            score += 1
        else:
            feedback.append(message)

    strength = "WEAK" if score <= 2 else "MEDIUM" if score <= 4 else "STRONG"
    return score, strength, feedback


password = getpass.getpass("Enter password: ")
score, strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
print(f"Score: {score}/6")
for item in feedback:
    print("-", item)
