user_input = input("Please enter a string: ")

for i in range(len(user_input) - 1):
        substring = user_input[i:i+2]
        print(substring)