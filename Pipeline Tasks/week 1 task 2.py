from abc import ABC, abstractmethod

# -----------------------------
# Abstract Base Class
# -----------------------------

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


# -----------------------------
# Subclasses
# -----------------------------

class Warrior(GameCharacter):
    def attack(self):
        return f"{self.name} swings a sword!"

    def defend(self):
        return f"{self.name} blocks with a shield."


class Mage(GameCharacter):
    def attack(self):
        return f"{self.name} casts a fireball!"

    def defend(self):
        return f"{self.name} creates a magic barrier."


class Archer(GameCharacter):
    def attack(self):
        return f"{self.name} shoots an arrow!"

    def defend(self):
        return f"{self.name} dodges quickly."


# -----------------------------
# Battle Simulation
# -----------------------------

def simulate_battle(characters):
    if len(characters) == 0:
        print("No characters to simulate.")
        return

    print("\n--- Battle Simulation ---")
    for c in characters:
        print(c.attack())
        print(c.defend())
    print("--- End of Battle ---")


# -----------------------------
# Menu Functions
# -----------------------------

def create_character():
    print("\nChoose character type:")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Archer")

    choice = input("Your choice: ")
    name = input("Enter character name: ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    else:
        print("Invalid choice.")
        return None


# -----------------------------
# Main Program
# -----------------------------

def main():
    characters = []

    while True:
        print("\nMenu:")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            ch = create_character()
            if ch is not None:
                characters.append(ch)
                print("Character created.")
        elif choice == "2":
            simulate_battle(characters)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid menu choice. Try again.")


main()