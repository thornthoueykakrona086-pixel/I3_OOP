class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
 
celsius = 25
fahrenheit = 77

print("Celsius:", celsius)
print("Fahrenheit:", Temperature.celsius_to_fahrenheit(celsius))
print("Kelvin:", Temperature.celsius_to_kelvin(celsius))

print("\nFahrenheit:", fahrenheit)
print("Celsius:", Temperature.fahrenheit_to_celsius(fahrenheit))