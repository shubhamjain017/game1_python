import random
n=random.randint(1,100)
print("Welcome to 'The Perfect Guess' game!")
print("I have selected a number between 1 and 100.")  
guess=0
a=-1
while(a!=n):
    a=int(input("Enter your guess: "))
    guess+=1
    if(a<n):
        print("Too low! Try again.")
    elif(a>n):
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {guess} attempts.")