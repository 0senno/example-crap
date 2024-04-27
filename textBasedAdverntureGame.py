import time

def intro():
    print("Welcome to the Mysterious Island Adventure!")
    print("You find yourself stranded on a mysterious island...")
    time.sleep(2)
    print("Your goal is to find a way off the island and return home.")
    time.sleep(2)
    print("Be careful! Danger lurks around every corner.")
    time.sleep(2)
    print("Let's begin!\n")

def explore_island():
    print("You start exploring the island...")
    time.sleep(2)
    print("As you walk through the dense jungle, you hear strange noises all around you.")
    time.sleep(2)
    print("Suddenly, you come across a fork in the path. Which way do you go?")
    time.sleep(2)
    while True:
        choice = input("Enter 'left' to go left or 'right' to go right: ").lower()
        if choice == "left":
            print("You decide to go left...")
            time.sleep(2)
            print("You encounter a wild animal and barely escape with your life!")
            time.sleep(2)
            print("You stumble upon an old abandoned cabin.")
            time.sleep(2)
            cabin()
            break
        elif choice == "right":
            print("You decide to go right...")
            time.sleep(2)
            print("You find a hidden cave and enter it cautiously.")
            time.sleep(2)
            cave()
            break
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")

def cabin():
    print("You cautiously enter the abandoned cabin...")
    time.sleep(2)
    print("Inside, you find some useful items and a map of the island.")
    time.sleep(2)
    print("You take the items and the map, then leave the cabin.")
    time.sleep(2)
    print("You continue your journey through the jungle.")
    time.sleep(2)
    explore_island()

def cave():
    print("You enter the dark cave...")
    time.sleep(2)
    print("You find a hidden treasure chest!")
    time.sleep(2)
    print("You open the chest and find a boat key inside.")
    time.sleep(2)
    print("You take the key and leave the cave.")
    time.sleep(2)
    print("You continue your journey through the jungle.")
    time.sleep(2)
    explore_island()

def main():
    intro()
    explore_island()

if __name__ == "__main__":
    main()
