from converter import celcius_to_fahrenheit

print("This is a temperature convert")

# using a try and exception block. Used to catch
# error that may occur in the code 

try:# this shows the error that has occured in script
    celcius = float(input("Enter a temperature in celcius: "))
    fahrenheit = celcius_to_fahrenheit(celcius)

    print(f"{celcius} is equal to {fahrenheit}")

except ValueError:
    print("Invalid input. Please enter a number")
