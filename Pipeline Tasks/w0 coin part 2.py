from coin_acceptor import CoinAcceptor

def main():
    acceptor = CoinAcceptor()

    while True:
        print("\nCoin Acceptor")
        print("1. Insert coin")
        print("2. Get amount of coins")
        print("3. Return coins")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acceptor.insertCoin()
            print("Coin inserted.")
        elif choice == "2":
            print(f"Amount of coins: {acceptor.getAmount()}")
        elif choice == "3":
            returned = acceptor.returnCoins()
            print(f"Returned {returned} coins.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()