import random

flag = True


def innerFunc(noOfLives):
    userNumber = 0
    lives = noOfLives
    global flag
    number = random.randint(1, 100)
    print(number)
    for i in range(lives):
        if flag:
            userNumber = int(input("Guess the number"))
            print(f"Your lives remaining {lives}")
            if userNumber < number:
                print("Too Low")
                lives = lives - 1
            elif userNumber > number:
                print("Too High")
                lives = lives - 1
            elif userNumber == number:
                print("Your guess was right")
                flag = False
                break
    else:
        print("You ran out of lives")

def noGuessing():
    level = input("Enter the level you want to try (easy or hard)?")
    if level == "easy":
        innerFunc(10)
    elif level == "hard":
        innerFunc(5)


noGuessing()
