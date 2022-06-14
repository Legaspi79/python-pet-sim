import menu

class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def set_name(self, name):
        self.name = name

def speak():

    match menu.main_menu.friendship:
        case 1: print(f"{pet.name} has nothing to say at the moment...")
        case 2: print(f"{pet.name} does a lil dance")
        case 3: print(f"{pet.name} is enjoying your company!")
        case 4: print(f"{pet.name} is curious about your feelings for them")
        case 5: print(f"{pet.name} loves you! They are glad that you two have become such good friends")


final_choice = False

while not final_choice:
    print("Choose a pet ")

    choice = int(input("1. Cat\n"
                       "2. Dog\n"
                       "3. Hedgehog\n"
                       "4. Penguin\n"
                       "5. Chicken\n"
                       "6. Turtle\n"))

    match choice:
        case 1:
            print("This is a very fat cat, they come with a bell. Pretty low maintenance as it likes to\n"
                  "laze around most of the time")
        case 2:
            print("This dog likes to slobber on all your belongings and has a HUGE appetite. Requests pets often.")
        case 3:
            print("This hedgehog is a cool customer, it comes with its own sunglasses. really likes to go to the beach")
        case 4:
            print("This Penguin is very busy and always seems to be expecting something....")
        case 5:
            print("This chicken seems to really enjoy your shirt.")
        case 6:
            print("This turtle has a habit of going missing, make sure to keep an eye on it")

    decide = input("Do you choose this pet? (y or n)\n").lower()

    if decide == "n":
        pass
    elif decide == "y":
        match choice:
            case 1:
                pet = Pet("", "Cat")
            case 2:
                pet = Pet("", "Dog")
            case 3:
                pet = Pet("", "Hedgehog")
            case 4:
                pet = Pet("", "Penguin")
            case 5:
                pet = Pet("", "Chicken")
            case 6:
                pet = Pet("", "Turtle")
        final_choice = True

while pet.name == "":
    pet.set_name(input("What will you name your new friend?: "))


print(f"{pet.name} sounds like a wonderful name for a {pet.species.lower()}!\n\n\n\n")