# Pet sim
import items
import menu
import shop
import pet


game = True
while game:
    print(f"{pet.pet.name} stares at you blankly...\n")

    action = int(input("What do you do?\n"
                       "1. Feed\n"
                       "2. Play\n"
                       "3. Converse\n"
                       "4. Shop\n"
                       "5. Check Condition\n"))
    match action:
        case 1:
            if menu.main_menu.hunger >= 10:
                print(f"\n{pet.pet.name} is still full!!!\n")
            else:
                for number, i in enumerate(items.food_inv):  #Display available food
                    print(number, i.name)
                print("\n")
                eat = int(input("\nWhat will you feed your pet?"))
                if items.food_inv[eat].hunger_add + menu.main_menu.hunger > 10:
                    print(f"{pet.pet.name} doesn't think they can finish that...")
                else:
                    print(f"{pet.pet.name} eats the {items.food_inv[eat].name}")

                    for i in items.food_inv[eat].is_liked:
                        if pet.pet.species == i:
                            menu.main_menu.friendship += 1
                            print(f"This is one of {pet.pet.name}'s favorites!!")

                    menu.main_menu.hunger += items.food_inv[eat].hunger_add
                    #menu.main_menu.friendship += items.food_inv[eat].friendship_add
                    menu.main_menu.mood += items.food_inv[eat].mood_add
                    if menu.main_menu.mood > 10:
                        menu.main_menu.mood = 10
                    items.food_inv.pop(eat)

        case 2:
            for number, i in enumerate(items.item_inv):  # Display available Items
                print(number, i.name)
            play = int(input(f"What would you like to give {pet.pet.name}?"))
            print(f"{pet.pet.name} {items.item_inv[play].action}")
            menu.main_menu.mood += items.item_inv[play].mood_add
            menu.main_menu.hunger -= 1
            if menu.main_menu.mood > 10:
                menu.main_menu.mood = 10

        case 3:
            pet.speak()

        case 4:
            print("1. Hakeem's Cafe\n"
                  "2. Pepper's Pet Shop\n")
            location = int(input("Where to?: \n"))
            if location == 1:
                shop.Shop.show_cafe(shop.hakeem)
            elif location == 2:
                shop.Shop.show_pet_store(shop.pepper)

        case 5:
            menu.main_menu.show_menu()
