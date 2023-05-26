import random as rnd

if __name__ == "__main__":
    PLAY_AGAIN = True
    while PLAY_AGAIN:
        secret = rnd.randrange(0,100)
        DID_GUESS = False
        for  num_guesses in range(0,10):
            guess = input(f" ({num_guesses+1}) Enter a number betwean 0 and 100: ")
            guess = int(guess)
            if guess < secret :
                print(f"The number {guess} is smaller")
            elif guess > secret :
                print(f"The number {guess} is bigger" )
            else:
                print(f"You have guessed the number {secret} after {num_guesses + 1}")
                DID_GUESS = True
                break
        if DID_GUESS is False:
            print(f"You loose the number is {secret}")
        play = input("Play again (Y/N)")
        if play == 'N':
            PLAY_AGAIN = False
            print("Good Bye")        
