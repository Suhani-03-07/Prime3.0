def Calculator(a,b,operation):
    if(operation == "+"):
        return a+b
    elif(operation == "-"):
        return a-b
    elif(operation == "*"):
        return a*b
    elif(operation == "/"):
        return a/b
    else:
        print("Invalid operation")
        
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
op = input("Enter a operator: ")

print(Calculator(num1,num2,op))