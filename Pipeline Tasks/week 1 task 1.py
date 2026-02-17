import csv
import base64
import os

# -----------------------------
# Device Classes
# -----------------------------

class IoTDevice:
    def __init__(self, deviceId, location, data):
        self.deviceId = deviceId
        self.location = location
        self.data = data

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "deviceId": self.deviceId,
            "location": self.location,
            "data": self.data
        }


class TemperatureSensor(IoTDevice):
    pass


class HumiditySensor(IoTDevice):
    pass


class MotionSensor(IoTDevice):
    pass


# -----------------------------
# Serialization
# -----------------------------

CSV_FILE = "iot_data.csv"
ENC_FILE = "iot_data.enc"
KEY = "secret123"   # simple key for XOR encryption


def serialize(devices):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "deviceId", "location", "data"])
        writer.writeheader()
        for d in devices:
            writer.writerow(d.to_dict())
    print("Data saved to CSV file.")


def deserialize():
    if not os.path.exists(CSV_FILE):
        print("CSV file does not exist.")
        return []

    devices = []
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["type"] == "TemperatureSensor":
                devices.append(TemperatureSensor(row["deviceId"], row["location"], row["data"]))
            elif row["type"] == "HumiditySensor":
                devices.append(HumiditySensor(row["deviceId"], row["location"], row["data"]))
            elif row["type"] == "MotionSensor":
                devices.append(MotionSensor(row["deviceId"], row["location"], row["data"]))
    print("Data loaded from CSV.")
    return devices


# -----------------------------
# Encryption / Decryption
# -----------------------------

def xor_encrypt(data, key):
    result = bytearray()
    key_bytes = key.encode()

    for i in range(len(data)):
        result.append(data[i] ^ key_bytes[i % len(key_bytes)])

    return bytes(result)


def encrypt_file():
    if not os.path.exists(CSV_FILE):
        print("CSV file not found.")
        return

    with open(CSV_FILE, "rb") as f:
        content = f.read()

    encrypted = xor_encrypt(content, KEY)
    encrypted = base64.b64encode(encrypted)

    with open(ENC_FILE, "wb") as f:
        f.write(encrypted)

    print("File encrypted.")


def decrypt_file():
    if not os.path.exists(ENC_FILE):
        print("Encrypted file not found.")
        return

    with open(ENC_FILE, "rb") as f:
        encrypted = f.read()

    decoded = base64.b64decode(encrypted)
    decrypted = xor_encrypt(decoded, KEY)

    with open(CSV_FILE, "wb") as f:
        f.write(decrypted)

    print("File decrypted.")


# -----------------------------
# Menu Functions
# -----------------------------

def add_device():
    print("Choose device type:")
    print("1 - TemperatureSensor")
    print("2 - HumiditySensor")
    print("3 - MotionSensor")

    choice = input("Your choice: ")

    deviceId = input("Device ID: ")
    location = input("Location: ")
    data = input("Data: ")

    if choice == "1":
        return TemperatureSensor(deviceId, location, data)
    elif choice == "2":
        return HumiditySensor(deviceId, location, data)
    elif choice == "3":
        return MotionSensor(deviceId, location, data)
    else:
        print("Invalid device type.")
        return None


# -----------------------------
# Main Program
# -----------------------------

def main():
    devices = []

    while True:
        print("\nMenu:")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            d = add_device()
            if d is not None:
                devices.append(d)
                print("Device added.")
        elif choice == "2":
            serialize(devices)
        elif choice == "3":
            devices = deserialize()
        elif choice == "4":
            encrypt_file()
        elif choice == "5":
            decrypt_file()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


main()