import items
import menu


class Shop:
    def __init__(self):
        # self.money = money
        pass

    def show_cafe(self):

        is_shopping = True
        while is_shopping:
            for number, i in enumerate(items.all_food):
                print(f"{number}. {i.name} - {i.price} shinies")
            choice = int(input("What would you like to buy?\n"))
            decision = input(f"Would you like to buy {items.all_food[choice].name}? (y or n)").lower()
            if decision == "y":
                items.food_inv.append(items.all_food[choice])
                menu.main_menu.money -= items.all_food[choice].price
                print(f"Your balance is now {menu.main_menu.money}")
                decision = input("Would you like to keep shopping? (y or n)\n").lower()
                if decision == 'y':
                    pass
                elif decision == 'n':
                    print("We hope to serve you again!\n\n")
                    is_shopping = False
            elif decision == "n":
                print("Okay, take your time browsing!")
            else:
                print("Not a valid command")

    def show_pet_store(self):
        is_shopping = True
        while is_shopping:
            for number, i in enumerate(items.itemStock):
                print(f"{number}. {i.name} - {i.price} shinies")
            choice = int(input("What would you like to buy?\n"))
            decision = input(f"Would you like to buy {items.itemStock[choice].name}? (y or n)").lower()
            if decision == "y":
                items.item_inv.append(items.itemStock[choice])
                menu.main_menu.money -= items.itemStock[choice].price
                print(f"Your balance is now {menu.main_menu.money}")
                decision = input("Would you like to keep shopping? (y or n)\n").lower()
                if decision == 'y':
                    pass
                elif decision == 'n':
                    print("We hope to serve you again!\n\n")
                    is_shopping = False
            elif decision == "n":
                print("Okay, take your time browsing!")
            else:
                print("Not a valid command")


hakeem = Shop()
pepper = Shop()
