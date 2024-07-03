import re
import sys
def zzbds():
    username = input("Username: ")
    password = input("Password: ")
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    m2 = re.match(r'^[0-9]{6,20}$', password)
    if m1 and m2:
        print("Username and password match")
        return True
    if not m1 or not m2:
        print("Username and password are incorrect")
        return False
if __name__ == '__main__':
    a = zzbds()
    if a:
        print("Yes")
    else:
        print("No")
    sys.exit(0)


