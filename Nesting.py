username= input("Enter username: ")
password= input("Enter password: ")

if(username == "admin" and password == "pass"):
    print("Login Successfull")
else:
    if(username != "admin"):
        print("Username entered wrong")
    else:
        print("Password entered wrong")        