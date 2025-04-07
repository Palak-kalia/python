# function to convert fahrenheit to celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Taking input from the user
fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)

# Display the result
print(fahrenheit_temp, "Fahrenheit is", round(celsius_temp, 2), "Celsius")
