import random

r = random.randint(1, 100)
count = 0
correct = 0

while count < 5:
    count += 1
    
    answer = input("Guess a number from 1 to 100: ")
    answer = int(answer)
    
    if answer < r:
        print("Number is too small")
    elif answer > r:
        print("Number is too big")
    else:
        print("Number is correct!")
        correct = 1
        break

if correct == 0:
    print(f"Sorry, you lost! The answer is {r}")
else:
    print(f"You won in {count} tries!")

