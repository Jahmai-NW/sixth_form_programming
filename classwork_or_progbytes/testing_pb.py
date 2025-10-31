def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "°C is equal to", fahrenheit, "F")


temp = float(input("Enter temperature in Celsius: "))
convert_temperature(temp)