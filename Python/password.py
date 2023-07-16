def is_strong_password(password):
    
    if len(password) < 8:
        return False
    # Check for uppercase, lowercase, and digits
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    # A loop to check every character in password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        if has_uppercase and has_lowercase and has_digit:
            break
    if not has_uppercase or not has_lowercase or not has_digit:
        return False
    # Check for special characters
    special_characters = "!@#$%^&*()-=_+[]{}|;:',.<>/?"
    has_special_char = any(char in special_characters for char in password)

    # It has lackings, it's not strong
    if not has_special_char:
        return False
    # Password passed all criteria, then it is strong
    return True
password = []
print("Enter five sample passwords : ")
for _ in range(5):
    sample = input()
    password.append(sample)
for i in password:
    if is_strong_password(i):
        print(f"\n {i} is a  Strong password!")
    else:
        print(f"\n {i} is a Weak password!")
