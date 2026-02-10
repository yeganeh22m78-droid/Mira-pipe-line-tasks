class TemperatureConverter:
    def __init__(self):
        self.__temperature = 0.0

    def setTemperature(self, temp: float) -> None:
        self.__temperature = temp

    def toCelsius(self) -> float:
        # Assume stored temperature is in Celsius already
        return self.__temperature

    def toFahrenheit(self) -> float:
        return (self.__temperature * 9/5) + 32

    def toKelvin(self) -> float:
        return self.__temperature + 273.15