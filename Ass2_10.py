num = 27
number = int(input("Guess the number:"))
if(number<num):
    print("Too Low!")
elif(number>num):
    print("Too High!")
else:
    print("Correct!")    