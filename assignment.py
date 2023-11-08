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


#toppings = ['1','2','3','4',]
#topping1 = (1.00)
#topping2 = (1.75)
#topping3 = (2.50)
#topping4 = (3.35)

tax_rate = (0.13)

pizza_yn = input("would you perhaps like to order a pizza (yes|no)")

# The Size selected by the customer
selected_size = 'None'

while True: 
    if pizza_yn.lower() == 'yes':   
        selected_size = input("What size would you like (L|XL)")
        
        while True:
            if selected_size in size_price_map:
                print(selected_size + ' is valid\n')
                #Put your logic to get the number of toppings here
                #Remember:
                #  Use the topping_price_map 
                #  using 'break' to exit the loop will take you out into the previous while loop
                #
                #Once you have size and toppings you need to get the pricing.
                #You do this by getting the value from each map using the key
                #Calculate:
                #  subtotal_amount (the price before tax)
                #  tax_amount (just the tax)
                #  total_amount (the total amount owed by the customer)
            else:
                print("Size entered is not valid")
                break

    else:
        break
 

