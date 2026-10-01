num = int(input("Enter a number: "))

def digit(a):
    while a>0:
        print(a%10)
        a=a//10
digit(num)        