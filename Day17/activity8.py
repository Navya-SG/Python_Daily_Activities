def password_check(password):
    c=0
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
    if any(char.islower() for char in password):
        c+=1
    if any(char.isupper() for char in password):
        c+=1
    if any(char.isdigit() for char in password):
        c+=1
    if any(char in special_characters for char in password):
        c+=1
    if len(password) >= 8:
        c+=1
    if c<=2:
        return "Weak"
    elif c<=4:
        return "Moderate"
    else:
        return "Strong"
password = input("Enter password: ")
print(password_check(password))