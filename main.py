import random

secret = random.randrange(1,100)
numguesses = 10


def compare(x,y):
    if x == y :
        return "ok"
    elif x > y :
        return "bigger"
    else:
        return "smaller"

while numguesses > 0:
    message = "you have {} guesses".format(numguesses)
    print(message)
    guess = input("Input a number [1 to 100]")
    numguesses = numguesses - 1
    result = compare(int(guess),secret)
    if result == "ok":
        print("You have guesed the number {} after {} guesses".format(secret,numguesses))
        break
    else:
        print("The number you have entered is {}".format(result))
