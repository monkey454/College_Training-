# nested if - else statement example
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Username not recognized.")  

# while loop example
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  

# break statement example
for i in range(10):
    if i == 5:
        break
    print(f"Current number is {i}") 

# continue statement example
attempts = 0
while attempts < 3:
    username = input("Enter your username: ")
    if username == "admin":
        print("Welcome back, admin!")
        break
    else:
        print("Invalid username, please try again.")
        attempts += 1
        if attempts == 3:
            print("Too many attempts, access denied.")
            continue

# nested loops example
for i in range(3):
    for j in range(2):
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")