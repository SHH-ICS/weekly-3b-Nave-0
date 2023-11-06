import math
large_price = (6.00)
extralarge_price = (10.00)
toppings = ['1','2','3','4',]
topping1 = (1.00)
topping2 = (1.75)
topping3 = (2.50)
topping4 = (3.35)
Tax = (1.13)
pizza_yn = input("would you perhaps like to order a pizza")
while True: 
    if pizza_yn.lower() == 'yes':   
        print("we will now take your order")
    else:
       print("order finished")
       break 
    var = input("what size pizza do you want, large or XL")
    print("how many toppings would you like")
    var = input(str("1,2,3 or 4"))
    if "large" and 1:
     print(large_price + topping1 * Tax)
     if "large" and 2: 
        print(large_price + topping2 * Tax)
        if "large" and 3: 
            print(large_price + topping3 * Tax)
        if "large" and 4: 
            print(large_price + topping4 * Tax)    