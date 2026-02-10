class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self) -> None:
        # Each coin increases amount by 1 and value by 0.20 (example coin value)
        # If you want a different coin value, you can change it here.
        self.__amount += 1
        self.__value += 0.20

    def getAmount(self) -> int:
        return self.__amount

    def returnCoins(self) -> int:
        returned = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return returned