import random

flag = True
while flag:
    num = input("Type a number for an limit: ")

    if num.isdigit():
        print("Let's Play!")
        num =  int(num)
        flag = False
    else:
        print("Invalid input! Try Again")

secret = random.randint(1,num)

guess = None
count = 0

while guess != secret:
    guess = input(f'Please try a number between 1 and {num} : ')
    if guess.isdigit():
        guess = int(guess)

        if guess == secret:
            print('You got it!')
        else:
            print("Please try again")
        count += 1
    else:
        print("Invalid input! Please enter a number.")

print("It tok you",count, "gusses!")