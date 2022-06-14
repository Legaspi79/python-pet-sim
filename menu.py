import happiness


class Menu:
    def __init__(self, hunger, mood, friendship, money):
        self.hunger = hunger
        self.mood = mood
        self.friendship = friendship
        self.money = money

    def show_menu(self):
        match main_menu.friendship:
            case 1:
                friendship_meter = "Aqcuaintances"
            case 2:
                friendship_meter = "Pals"
            case 3:
                friendship_meter = "Buddies"
            case 4:
                friendship_meter = "Friends"
            case 5:
                friendship_meter = "Besto Furendos"

        print(f"Hunger: {self.hunger}\n"
              f"Mood: {self.mood}\n"
              f"Friendship: {friendship_meter}\n"
              f"Shinies: {self.money}")


main_menu = Menu(5, 5, 1, 300)










