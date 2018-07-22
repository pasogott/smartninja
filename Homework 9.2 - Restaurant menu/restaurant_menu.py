from datetime import datetime

daily_menu = {}

def valid_date_input():
    valid_input = False
    while valid_input == False:
        date_input = raw_input("Whats the date today? ")
        try:
            d = datetime.strptime(date_input, "%d.%m.%Y")
            valid_input = True
        except:
            print "That was not a valid date! The correct format is DDMMYYYY!"
    return d


if __name__ == '__main__':

    date_input = valid_date_input().strftime("%d.%m.%Y")
    dish_input = raw_input("What is the menu today? ")
    price_input = raw_input("How much is the menu today? ")

    try:
        price_input = float(price_input)
        daily_menu[date_input] = {dish_input: price_input}

        print menu[daily_menu]

    except ValueError:
        print "This was not a valid input for the price!"

    with open("menu.txt", "a") as f:
        content = f.write(str(daily_menu))