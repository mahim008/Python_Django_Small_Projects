import re
def strength(password):
    strong = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    medium = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"

    if re.match(strong, password):
        return "Strong Password"
    elif re.match(medium, password):
        return "Medium Password"
    else:
        return "Weak"


password = input("Enter any password to check : ")
print(f"Your password goes under : {strength(password)}")
