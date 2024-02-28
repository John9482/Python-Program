class Temperature:
    def convert_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    def convert_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")


# Prompting user for temperature
temperature = float(input("Enter temperature: "))

# Creating Temperature object
temp_obj = Temperature()

# Converting temperature
temp_obj.convert_fahrenheit(temperature)
temp_obj.convert_celsius(temperature)
