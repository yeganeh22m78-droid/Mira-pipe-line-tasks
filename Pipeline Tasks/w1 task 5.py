# -----------------------------
# Base Class
# -----------------------------

class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position   # could be something simple like a number or text

    def interact(self):
        # This will be overridden by subclasses
        pass


# -----------------------------
# Subclasses
# -----------------------------

class Player(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position)
        self.health = health

    def interact(self):
        return f"Player {self.name} explores the world at position {self.position}."


class NPC(Entity):
    def __init__(self, name, position, dialogue):
        super().__init__(name, position)
        self.dialogue = dialogue

    def interact(self):
        return f"NPC {self.name} says: '{self.dialogue}'."


class Object(Entity):
    def __init__(self, name, position, description):
        super().__init__(name, position)
        self.description = description

    def interact(self):
        return f"Object {self.name} can be examined: {self.description}."


# -----------------------------
# Polymorphic Function
# -----------------------------

def interact_with_entities(entities):
    if len(entities) == 0:
        print("No entities to interact with.")
        return

    print("\n--- Interactions ---")
    for e in entities:
        print(e.interact())
    print("--------------------")
    

# -----------------------------
# Menu Functions
# -----------------------------

def add_entity():
    print("\nChoose entity type:")
    print("1 - Player")
    print("2 - NPC")
    print("3 - Object")

    choice = input("Your choice: ")
    name = input("Enter name: ")
    position = input("Enter position: ")

    if choice == "1":
        health = input("Enter health: ")
        return Player(name, position, health)

    elif choice == "2":
        dialogue = input("Enter dialogue: ")
        return NPC(name, position, dialogue)

    elif choice == "3":
        description = input("Enter object description: ")
        return Object(name, position, description)

    else:
        print("Invalid choice.")
        return None


# -----------------------------
# Main Program
# -----------------------------

def main():
    entities = []

    while True:
        print("\nMenu:")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            e = add_entity()
            if e is not None:
                entities.append(e)
                print("Entity added.")
        elif choice == "2":
            interact_with_entities(entities)
        elif choice == "3":
            print("Exiting simulation.")
            break
        else:
            print("Invalid menu choice. Try again.")


main()