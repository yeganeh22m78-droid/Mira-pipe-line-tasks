

class CryptoWallet:
    def __init__(self, walletId):
        self._walletId = walletId      
        self._balance = 0.0            
        self._history = []             

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        self._history.append(f"Deposited {amount}")
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        if amount > self._balance:
            print("Not enough balance.")
            return
        self._balance -= amount
        self._history.append(f"Withdrew {amount}")
        print("Withdrawal successful.")

    def check_balance(self):
        return self._balance

    def transaction_history(self):
        if len(self._history) == 0:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in self._history:
                print(t)
            print("---------------------------")



def create_wallet():
    walletId = input("Enter wallet ID: ")
    return CryptoWallet(walletId)


def deposit_to_wallet(wallets):
    walletId = input("Enter wallet ID: ")
    amount = float(input("Enter deposit amount: "))

    for w in wallets:
        if w._walletId == walletId:
            w.deposit(amount)
            return
    print("Wallet not found.")


def withdraw_from_wallet(wallets):
    walletId = input("Enter wallet ID: ")
    amount = float(input("Enter withdrawal amount: "))

    for w in wallets:
        if w._walletId == walletId:
            w.withdraw(amount)
            return
    print("Wallet not found.")


def check_wallet_balance(wallets):
    walletId = input("Enter wallet ID: ")

    for w in wallets:
        if w._walletId == walletId:
            print("Balance:", w.check_balance())
            return
    print("Wallet not found.")


def show_history(wallets):
    walletId = input("Enter wallet ID: ")

    for w in wallets:
        if w._walletId == walletId:
            w.transaction_history()
            return
    print("Wallet not found.")




def main():
    wallets = []

    while True:
        print("\nMenu:")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            w = create_wallet()
            wallets.append(w)
            print("Wallet created.")
        elif choice == "2":
            deposit_to_wallet(wallets)
        elif choice == "3":
            withdraw_from_wallet(wallets)
        elif choice == "4":
            check_wallet_balance(wallets)
        elif choice == "5":
            show_history(wallets)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid menu choice. Try again.")


main()