#Greetings
print ("Welcome to Aayushi's Restaurant!")
#Menu
print ("Here is the menu for today:")
menu = {
    "Pizza" : 558,
    "Pasta" : 350,
    "Paneer Momo" : 150,
    "Veg Momo" : 110,
    "Coffee" : 89,
    "Noodles" : 120,
    "Manchurian" : 99,
    "Pizza Puff" : 85,
    "Veg Biryani": 200,
    "Chilli Paneer": 140,
    "Spring Roll": 130,
    "Fried Rice": 115,
    "Schezwan Rice": 125,
    "Masala Dosa": 90,
    "Samosa": 25,
    "Veg Burger": 70,
    "French Fries": 60,
    "Cheese Sandwich": 80,
    "Hakka Noodles": 130,
    "Paneer Tikka": 160,
    "Veg Roll": 75,
    "Veg Salad": 50,
    "Ice Cream": 100,
    "Soft Drink": 40,
    "Lassi": 60,
    "Fruit Juice": 50,
    "Tea": 30,
    "Hot Chocolate": 70,
    "Chocolate Shake": 90,
    "Milkshake": 80,
    "Paneer Butter Masala": 220,
    "Dal Makhani": 180,
    "Veg Thali": 250,
}
#Variable for bill amount
menu_total = 0
#Taking order
order_1 = input("Enter the item you would like to have today: ") 
if order_1 in menu:
    menu_total+= menu[order_1]
    print(f"{order_1} has been added to your order. Current total: {menu_total}")
else:
    print("Sorry, that item is not on the menu.")
    
input_more = input("Would you like to order more items? (yes/no): ").strip().lower() 
while input_more == "yes":
    order_2 = input("Enter the next item you would like to have: ")
    if order_2 in menu:
        menu_total += menu[order_2]
        print(f"{order_2} has been added to your order. Current total: {menu_total}")
    else:
        print("Sorry, that item is not on the menu.")
    input_more = input("Would you like to order more items? (yes/no): ").strip().lower()
  #final statements
    print("Thank you for your order!")
    print(f"Your total bill is: {menu_total} INR")
    print("Enjoy your meal!")  
      
    
    
    
    


    
    
    
    
