def getPword(attempt):
    if attempt == 1:
        ask = input("Enter password: ")
    else:
        ask = input("Enter password again: ")

    password = ask

    while len(password) < 6 or len(password) > 8:
        print("Error - password must be 6 to 8 characters long")
        if attempt == 1:
            password = input("Enter password: ")
        else:
            password = input("Enter password again: ")
    return password

while True:
    password1 = getPword(1)
    password2 = getPword(2)

    if password1 != password2:
        print("Error: passwords do not match")
    else:
        break

print("Password change successful")
