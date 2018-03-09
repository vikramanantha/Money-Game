# -*- coding: ascii -*-
import time


score = 0
items = []
rate = 1
hired = []

def money(rate, items):
    global score
    print("\nYou have $" + str(score) + "\n")
    print("\nYou have four options. You can")
    options = input("Hit Enter to get money \nType 'Hire' to hire people to do things \nType 'Buy' to buy things "
                    "\nType 'Show' to show the things you have \n").lower()
    if options == '':
        score += rate

    elif options == 'hire':
        hire_objs = [{"Number": "1", "name": 'Lemonade Stand', 'price': 5, 'sal': 1, 'earn': 10},
                    {"Number": "2", "name": 'Car Wash', 'price': 15, 'sal': 1, 'earn': 30},
                    {"Number": "3", "name": 'Car Wash COMPANY', 'price': 100, 'sal': 2, 'earn': 0},
                    {"Number": "4", "name": 'Company', 'price': 300, 'sal': 4, 'earn': 0},
                    {"Number": "5", "name": 'Butler', 'price': 1000000, 'sal': 10, 'earn': 10}]
        hire_options = ""
        for obj in hire_objs:
            hire_options += obj["Number"] + ") " + "($" + str(obj['price']) + ") " + obj["name"] + ": Earn $" + str(obj['earn']) + " And " + str(obj["sal"]) + "x the salary" + "\n"
        hire_input_string = "You can buy stuff here! \n" + hire_options
        hopt = input(hire_input_string)
        for i in hire_objs:
            if hopt == i["Number"]:
                if score >= i["price"]:
                    score -= i["price"]
                    hired.append(i["name"])
                    score += i["earn"]
                    rate *= i["sal"]
                    print("You hired the " + i["name"])
                    money(rate, items)
                else:
                    print("Sorry, You cannot buy this item. It is too expensive. Try something cheaper. ")
                return
        print("You didn't select a vaild item.")

    elif options == 'show':
        print("You have $" + str(score))
        print("Your Salary is $" + str(rate))
        print("You have " + str(items) + " items. ")
        print("You have had " + str(hired) + " hired. ")
        input("Press any key to continue.")


    elif options == 'buy':
        buy_objs = [{"Number": "1", "name": 'Vending Machine Snack', 'price': 2}, {"Number": "2", "name": 'Apple', 'price': 5},
                    {"Number": "3", "name": 'Pack of Pencils', 'price': 10}, {"Number": "4", "name": 'LEGO Set', 'price': 20},
                    {"Number": "5", "name": 'Book', 'price': 25}, {"Number": "6", "name": 'Gift Card', 'price': 50},
                    {"Number": "7", "name": 'Good Shoes', 'price': 100}, {"Number": "8", "name": 'Phone', 'price': 500},
                    {"Number": "9", "name": 'Car', 'price': 50000}, {"Number": "10", "name": 'House', 'price': 500000}]
        buy_options = ""
        for obj in buy_objs:
            buy_options += obj["Number"] + ") " + obj["name"] + ": " + "$" + str(obj['price']) + "\n"
        buy_input_string = "You can buy stuff here! \n" + buy_options
        bopt = input(buy_input_string)
        for i in buy_objs:
            if bopt == i["Number"]:
                if score >= i["price"]:
                    score -= i["price"]
                    items.append(i["name"])

                    money(rate, items)
                else:
                    print("Sorry, You cannot buy this item. It is too expensive. Try something cheaper. ")
        print("You didn't select a vaild item")

    elif options == 'quit':
        sys.exit(0)

    money(rate, items)

money(rate, items)