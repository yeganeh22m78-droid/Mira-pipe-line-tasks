

class SmartDevice:
    def __init__(self, deviceName, status="OFF"):
        self.deviceName = deviceName
        self.status = status

    def operate(self):
    
        pass


class SmartLight(SmartDevice):
    def __init__(self, deviceName, brightness):
        super().__init__(deviceName)
        self.brightness = brightness

    def operate(self):
        return f"{self.deviceName} light is now ON at brightness {self.brightness}."


class SmartThermostat(SmartDevice):
    def __init__(self, deviceName, temperature):
        super().__init__(deviceName)
        self.temperature = temperature

    def operate(self):
        return f"{self.deviceName} thermostat set to {self.temperature}°C."


class SmartLock(SmartDevice):
    def __init__(self, deviceName, locked=True):
        super().__init__(deviceName)
        self.locked = locked

    def operate(self):
        if self.locked:
            return f"{self.deviceName} lock is now UNLOCKED."
        else:
            return f"{self.deviceName} lock is now LOCKED."


# -----------------------------
# Polymorphic Function
# -----------------------------

def operate_devices(devices):
    if len(devices) == 0:
        print("No devices to operate.")
        return

    print("\n--- Operating Smart Devices ---")
    for d in devices:
        print(d.operate())
    print("--- Done ---")


# -----------------------------
# Menu Functions
# -----------------------------

def add_device():
    print("\nChoose device type:")
    print("1 - Smart Light")
    print("2 - Smart Thermostat")
    print("3 - Smart Lock")

    choice = input("Your choice: ")
    name = input("Device name: ")

    if choice == "1":
        brightness = input("Brightness (1-100): ")
        return SmartLight(name, brightness)

    elif choice == "2":
        temp = input("Temperature (°C): ")
        return SmartThermostat(name, temp)

    elif choice == "3":
        lock_state = input("Locked? (yes/no): ").lower()
        locked = True if lock_state == "yes" else False
        return SmartLock(name, locked)

    else:
        print("Invalid choice.")
        return None


# -----------------------------
# Main Program
# -----------------------------

def main():
    devices = []

    while True:
        print("\nMenu:")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            d = add_device()
            if d is not None:
                devices.append(d)
                print("Device added.")
        elif choice == "2":
            operate_devices(devices)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid menu choice. Try again.")


main()