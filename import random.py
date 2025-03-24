import random
pin_random= random.randint(1000,9999)

user_number = int(input("Enter a 4 digit PIN Code: "))
if len(str(user_number)) != 4:
    print("Please Enter 4 digits")
elif user_number == pin_random:
    print("Seccess! PIN Code matched")
else:
    print("Failure! PIN Code didn't matched")
    print(f"The Computer generated this PIN {pin_random}")