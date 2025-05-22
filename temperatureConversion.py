def convertToFahrenheit(degreesCelsius):
    
    return degreesCelsius * (9/5) + 32

def convertToCelsius(degreesFahrenheit):
    
    return (degreesFahrenheit - 32) * (5/9)


input_temp = int(input("Enter the temperature value: "))

print("The temperature in Fahrenheit for the given Temperature value is: ",convertToFahrenheit(input_temp))
print("The temperature in Celsius for the given Temperature value is: ",convertToCelsius(input_temp))

