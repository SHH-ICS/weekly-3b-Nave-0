import math
size_price_map = {
    'L' : 6.00,
    'XL' : 10.00
}

topping_price_map = { 
    '1' : 1.00,
    '2' : 1.75,
    '3' : 2.50,
    '4' : 3.35
}
tax_rate = (0.13)
pizza_yn = input("would you perhaps like to order a pizza (yes|no)")
selected_size = 'None'
number_of_toppings = 'None'
while True: 
    if pizza_yn.lower() == 'yes':   
        selected_size = input("What size would you like (L|XL)")
        while True:
            if selected_size in size_price_map:
                print()
            else:
                print("Size entered is not valid")
                break 
            while True: 
                number_of_toppings = input("How many topping would you like (1,2,3,4)") 
                if number_of_toppings in topping_price_map:
                    price_of_toppings = topping_price_map[number_of_toppings]
                    price_of_pizza = size_price_map[selected_size]
                    subtotal = price_of_pizza + price_of_toppings
                    print("Subtotal: " + str(subtotal))
                    tax_amount = subtotal * tax_rate
                    print("Tax Amount: " + str(tax_amount))
                    total_cost = subtotal + tax_amount
                    print("Total Cost: " + str(total_cost))
                    break
                else:
                    print("amount of toppings entered is not valid")
                    break


