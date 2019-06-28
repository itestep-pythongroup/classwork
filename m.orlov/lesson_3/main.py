#!/usr/bin/python3.7


def print_hello(print,input):
    print("hello world")

    
def print_yes_or_no(print,input):
    x = input()
    if x == "y":
        print("yes")
    elif x == "n":
        print("no")
    else:
        print("------")

        
def make_check(print,input):
    divisor = 1.0
    if input("is-usd?") == "y":
        divisor = 27.0
    
    beef = 40.0/divisor
    beef_amount_in_kg = 1.3
    chicken = 56.0/divisor
    chicken_amount_in_kg = 2.3
    tomatoes = 45.0/divisor
    tomatoes_amount_in_kg = 3.7
    avocado  = 22.0/divisor
    avocado_amount_in_pieces = 5.0
    
    total = beef*beef_amount_in_kg\
            +chicken*chicken_amount_in_kg\
            +tomatoes_amount_in_kg*chicken_amount_in_kg\
            +avocado*avocado_amount_in_pieces
    
    tax = total * 0.20
    total_and_tax = tax + total
    
    print("Beef__________","(",beef_amount_in_kg, ")",beef*beef_amount_in_kg)
    print("Chicken_______","(",chicken_amount_in_kg,")",chicken*chicken_amount_in_kg)
    print("Tomatoes______","(",tomatoes_amount_in_kg,")",tomatoes_amount_in_kg*chicken_amount_in_kg)
    print("Avocado_______","(",avocado_amount_in_pieces,")",avocado*avocado_amount_in_pieces)
    print("Tax___________ ( 20% )",tax)
    print("Total+Tax_____","       ",total_and_tax)
