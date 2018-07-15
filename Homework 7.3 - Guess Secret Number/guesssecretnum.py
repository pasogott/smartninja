secret = 4

while True:
    guess = raw_input("Guess the secret number: ")
    if int(guess) == secret:
        print "Congratulations, the secret number is " + guess
        break
    else:
        print "Sorry wrong number, Try again"
