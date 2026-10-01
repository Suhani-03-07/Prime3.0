num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

def Average(a,b,c):
    avg = int((a+b+c)/3)
    return avg

print(Average(num1,num2,num3))

#def sum(a,b=1): # here b is the default parameter which means if only 1 value gets passed then b will be 1
#    return a+b
#print(sum(5))