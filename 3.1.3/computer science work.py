coupon = 0
fries = 0.0
sandwich = 0.0
drink = 0.0
ketchup = 0.0
ree = []
sandwich_order = input("would you like a beef sandwich [6.25] a chicken sandwich [5.25] or a tofu sandwich[5.75]")
if sandwich_order == ("beef"):
    sandwich = 6.25
    coupon += 1
    ree.append("beef")
elif sandwich_order == ("chicken"):
    sandwich = 5.25
    coupon += 1
    ree.append("chicken")
elif sandwich_order == ("tofu"):
    sandwich = 5.75
    coupon += 1
    ree.append("tofu")
print(sandwich_order + " " + str(sandwich))
# drink time wooooooooo
drink_order = input("Large drink(2.25) medium drink(1.75) small drink (1.00) or no?")
if drink_order == ("large"):
    drink = 2.25
    coupon += 1
    ree.append("Large drink")
elif drink_order == ("medium"):
    drink = 1.75
    coupon += 1
    ree.append("Medium drink")
elif drink_order == ("small"):
    drink = 1.00
    coupon += 1
    ree.append("Small drink")
elif drink_order == ("no"):
    drink = 0.0
# fries woop woop
fry_order = input("large fries(2.00) medium fries(1.50) small fries(1.00)")
if fry_order == ("no"):
    fries = 0.0
elif fry_order == ("medium"):
    fries = 1.50
    coupon += 1
    ree.append("Medium fries")
elif fry_order == ("small"):
    megasize = input("would you like to megasize that?")
    if megasize == ("yes"):
        fries = 2.00
        coupon += 1
        ree.append("Large fries")
        print("succesfully MEGASIZED")
    elif megasize == "no":
        fries = 1.00
        coupon += 1
        ree.append("Small fries")
elif fry_order == "large":
    fries = 2.00
    coupon += 1
    ree.append("Large fries")
    # ketchup time
ketchup_packets = input("how many ketchup packets would you like? (0.25) each")
ketchup = (float(ketchup_packets) * 0.25)
ree.append(ketchup_packets)
total = (sandwich + drink + fries + ketchup)
if coupon == 3:
    total -= 1
    print("you get a discount")
print("your order is " + str(ree))
print("your total is " + str(total))
