
x = range(1, 100)

while True:
    input = raw_input("Select a number between 1 and 100: ")
    try:
        input_num = int(input)
        if input_num in x:
            for i in x:
                if i == input_num:
                    print "Your number was {}".format(i)
                    break
                elif i % 3 == 0 and i % 5 == 0:
                    print "Fizzbuzz"
                elif i % 3 == 0:
                    print "Fizz"
                elif i % 5 ==0:
                    print "Buzz"
                else:
                    print i
        else:
            print "You have to select an integer between 1 and 100! Try again: "
    except ValueError:
        print "ERROR! Not a number! Try again :"


