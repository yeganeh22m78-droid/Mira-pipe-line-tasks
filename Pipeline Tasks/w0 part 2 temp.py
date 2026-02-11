from temperature_converter import TemperatureConverter

def main():
    converter = TemperatureConverter()

    while True:
        print("\nTemperature Converter")
        print("1. Set temperature (Celsius)")
        print("2. Convert to Celsius")
        print("3. Convert to Fahrenheit")
        print("4. Convert to Kelvin")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                temp = float(input("Enter temperature in Celsius: "))
                converter.setTemperature(temp)
                print("Temperature set.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            print(f"Temperature in Celsius: {converter.toCelsius():.2f}")
        elif choice == "3":
            print(f"Temperature in Fahrenheit: {converter.toFahrenheit():.2f}")
        elif choice == "4":
            print(f"Temperature in Kelvin: {converter.toKelvin():.2f}")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()