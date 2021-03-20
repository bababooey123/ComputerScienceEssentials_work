coupon = 0
fries = 0.0
sandwich = 0.0
drink = 0.0
ketchup = 0.0
sandwich_order = input("would you like a beef sandwich [6.25] a chicken sandwich [5.25] or a tofu sandwich[5.75]")
if sandwich_order == ("beef"):
    sandwich = 6.25
    var = coupon + 1
elif sandwich_order == ("chicken"):
    sandwich = 5.25
    var = coupon + 1
elif sandwich_order == ("tofu"):
    sandwich = 5.75
    var = coupon + 1
print(sandwich_order + " " + str(sandwich))
# drink time wooooooooo
drink_order = input("Large drink(2.25) medium drink(1.75) small drink (1.00) or no?")
if drink_order == ("large"):
    drink = 2.25
    var = coupon + 1
elif drink_order == ("medium"):
    drink = 1.75
    var = coupon + 1
elif drink_order == ("small"):
    drink = 1.00
    var = coupon + 1
elif drink_order == ("no"):
    drink = 0.0
# fries woop woop
fry_order = input("large fries(2.00) medium fries(1.50) small fries(1.00)")
if fry_order == ("no"):
    fries = 0.0
elif fry_order == ("medium"):
    fries = 1.50
    var = coupon + 1
elif fry_order == ("small"):
    megasize = input("would you like to megasize that?")
    if megasize == ("yes"):
        fries = 2.00
        print("succesfully MEGASIZED")
    elif megasize == "no":
        fries = 1.00
elif fry_order == "large":
    fries = 2.00
    var = coupon + 1
    # ketchup time
ketchup_packets = input("how many ketchup packets would you like? (0.25) each")
ketchup = (float(ketchup_packets) * 0.25)
total = (sandwich + drink + fries + ketchup)
if coupon == 3:
    total = (total - 1)
print("your order is " + str(sandwich_order) + " sandwich " + str(drink_order) + " drink " + str(fry_order) + " fries " + str(ketchup_packets) + " ketchup packet your total is " + str(total))