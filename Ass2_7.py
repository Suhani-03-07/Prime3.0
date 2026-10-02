while True:
    num = input("Enter a number: ")

    if(num == "Quit" or num == "quit"):
        break
    else:
        if(int(num) >= 0):
            print("The number you entered is positive")
            
        else:
            print("The number you entered is negative")   
            
             
