class Celsius:
    def __init__(self, temp=0):
        self._temperature = temp

    def to_fahrenheit(self):
        return (self.temperature * (9 / 5)) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value


t = Celsius(10)
print(t.to_fahrenheit())  # 50.0
t.temperature = 24
print(t.temperature)  # 24
print(t.to_fahrenheit())  # 75.2
