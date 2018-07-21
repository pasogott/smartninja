name = raw_input("What is your name? ")
print "Hi " + name + ", let us convert some units:"


def calc_unit(num):
    miles = num * 0.62137
    return str(num) + " Kilometers are " + str(miles) + " Miles!"


while True:
    try:
        num = float(raw_input("Enter a number of kilometers: "))
        miles = calc_unit(num)
        print miles

        input = raw_input("Do you want to convert again? yes or no? ")

        while input.lower() not in  ("no", "yes"):
            input = raw_input("you have to enter yes or no!")

        if input.lower() == "no":
            print "Thank you for converting, goodbye!"
            break
        elif input.lower() == "yes":
            continue
    except ValueError:
        print "You have to enter a digit! Try again: "

