import pet

class Items:
    def __init__(self, name, price, mood_add, is_liked):
        self.name = name
        self.price = price
        self. mood_add = mood_add
        self.is_liked = is_liked


class Toys(Items):
    def __init__(self, name, price, mood_add, is_liked, action):
        super().__init__(name, price, mood_add, is_liked)
        self.action = action


class Food(Items):
    def __init__(self, name, price, mood_add, is_liked, hunger_add):
        super().__init__(name, price, mood_add, is_liked)
        self.hunger_add = hunger_add




'''Toys'''
tennisBall = Toys("Tennis Ball", 0, 1, [], f"plays with the ball")
pollyPocket = Toys("Polly Pocket", 30, 2, [], f"changes the clothes on Polly")
ballOfYarn = Toys("Ball 'o' Yarn", 5, 1, [], f"nudges the ball of yarn around a few times")
gameboy = Toys("Gameboy Color", 200, 5, [], f"is trying to speedrun Wario Land 3!! Look at em go!")
cellphone = Toys("Toy Cellphone", 20, 2, [], f"is pretending to be a businessman..."
                                            f"They're in a meeting!")
'''Food'''
petFood = Food("Pet Food", 1, 0, [], 1)
shortcake = Food("Strawberry Shortcake", 20, 2, ["Cat"], 2)
cheeseTart = Food("Sweet Cheese Tart", 15, 1, ["Turtle"], 0)
snoCone = Food("Sno-Cone", 10, 3, ["Hedgehog"], 0)
tiramisu = Food("Tiramisu", 40, 3, ["Chicken"], 2)
sundae = Food("Sundae", 35, 3, ["Penguin"], 1)
donut = Food("Pink Sprinkled Donut", 5, 2, ["Dog"], 0)
dinoNuggets = Food("Dino Nuggets", 10, 3, 5, 3)
shawarma = Food("Shawarma", 15, 2, 2, 2)
clamChowder = Food("Clam Chowder", 20, 2, 1, 4)


itemStock = [pollyPocket, ballOfYarn, gameboy, cellphone]
item_inv = [tennisBall]

all_food = [dinoNuggets, shawarma, clamChowder, shortcake, cheeseTart, snoCone, tiramisu, sundae, donut]
food_inv = [petFood, shortcake, shortcake]



