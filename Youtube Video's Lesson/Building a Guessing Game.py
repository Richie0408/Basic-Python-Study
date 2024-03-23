import random
answer = random.choice(range(10))
guess_count = 1
guess_limit = 3
chance = 3
print("Guess a number between 1 until 10")
print("You have 3 changes")

while guess_count <= guess_limit:
    guess = int(input("Guess = "))
    print("============================================")
    if 0<=guess<=10:
        guess_count += 1
        chance -= 1
        print("============================================")
        if guess != answer:
            if chance != 0:
                print("You have", chance, "more chance")
            else:
                print("Try again next time...")
                break
        else:
            print("Nice, you're in")
            break
    else:
        print("You must enter a number between 1 until 10")
else:
    print("Try again next time...")
    print(answer)
