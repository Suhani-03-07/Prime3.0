number = int(input("Enter a number"))
def Is_Prime(n):
    if(n == 2):
        print("2 is a prime number")
    elif(n>2):
        for i in range(2,n-1,1):
                if(n%i ==0):
                    print(n,"is not a prime number") 
                    return  
        print(n,"is a prime number")
                     
Is_Prime(number)