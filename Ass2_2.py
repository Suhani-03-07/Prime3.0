def Even(a,b):
    for i in range(a,b+1):
        if(i%2 == 0):
            print (i)
        
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))    
Even(num1,num2)      