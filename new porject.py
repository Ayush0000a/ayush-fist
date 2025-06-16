 #define the menu of restaurant
menu = {
    'pizza' :50,
    'pasta':60,
    'burger':90,
    'salad':70,
    'coffee':90, 
}

#greet  
print("welcome to python restaurant")
print( "pizza :Rs50\npasta:60\nburger:90\nsalad':70\ncoffee:90")


order_total = 0 
#80+70=150
        
item_1 = input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1}has been added to your order")
else:
    print(f"ordered item {item_1}is not avaialable yet")

another_order = input("Do you want to add another item? (yes/No) ")
if another_order =="yes":
    item_2 = input("enter the name of secont item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"ordered item {item_2} is not avaialable!")
print(f"the total amount of items to pay  is {order_total}")                          