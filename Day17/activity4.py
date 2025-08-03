'''
f_name=input()
l_name=input()
u_name=input()
pwd=input()
if pwd!=u_name and pwd!=f_name and len(pwd)>=10 and pwd.upper() and pwd.lower():
    print("Valid")
else:
    print("not valid")

#and pwd!=l_name and len(pwd)>=10 and pwd.upper() and pwd.lower()
    '''

u_name = input("Enter username: ")
f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
pwd = input("Enter password: ")

def pwd_valid(u_name, f_name, l_name, pwd):
    if pwd == u_name:
        return "Password should not be the same as username"
    if pwd == f_name or pwd == l_name:
        return "Password should not be same as first or last name"
    if len(pwd) < 10:
        return "Password must be at least 10 characters long"
    if not pwd.isalnum():
        return "Password must be alphanumeric"
    if pwd.lower() == pwd or pwd.upper() == pwd:
        return "Password must include both uppercase and lowercase letters"
    return "Password is valid"

print(pwd_valid(u_name, f_name, l_name, pwd))

