def email(a):
    if ("@" in a) and ("." in a):
        print("This email is valid")
    else:
        print("This email is not valid")
a = input("Enter your email:")
email(a)