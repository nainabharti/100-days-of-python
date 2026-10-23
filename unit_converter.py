def length_converter():
    value = float(input("Enter value: "))
    convert_from = input("Convert from (km/m/cm): ").lower()
    convert_to = input("Convert to (km/m/cm): ").lower()
    if convert_from == "km" and convert_to == "m":
        result = value *1000
    elif convert_from == "m" and convert_to == "km":
        result = value/1000
    elif convert_from == "m" and convert_to == "cm":
        result = value * 100
    elif convert_from == "cm" and convert_to == "m":
        result = value/100
    elif convert_from == "km" and convert_to == "cm":
        result = value*100000
    elif convert_from == "cm" and convert_to == "m":
        result = value/100000
    elif convert_from == convert_to and convert_from in ["km", "m", "cm"]:
        result = value
    else:
        print("Invalid unit conversion!")
        return
    print(f"Converted value: {result}")

def weight_converter():
    value = float(input("Enter value: "))
    convert_from = input("Convert from (kg/g): ").lower()
    convert_to = input("Convert to (kg/g): ").lower()
    if convert_from == "kg" and convert_to == "g":
        result = value*1000
    elif convert_from == "g" and convert_to == "kg":
        result = value/1000
    elif convert_from == convert_to and convert_from in["kg", "g"]:
        result = value
    else:
        print("Invalid unit conversion!")
        return
    print(f"Converted value: {result}")

def temperature_converter():
    value = float(input("Enter temperature: "))
    convert_from = input("Convert from (C/F/K): ").upper()
    convert_to = input("Convert to (C/F/K): ").upper()

    if convert_from == convert_to and convert_from in ["C", "F", "K"]:
        result = value

    elif convert_from == "C" and convert_to == "F":
        result = (value * 9/5) + 32
    elif convert_from == "F" and convert_to == "C":
        result = (value - 32) * 5/9

    elif convert_from == "C" and convert_to == "K":
        result = value + 273.15
    elif convert_from == "K" and convert_to == "C":
        result = value - 273.15

    elif convert_from == "F" and convert_to == "K":
        result = (value - 32) * 5/9 + 273.15
    elif convert_from == "K" and convert_to == "F":
        result = (value - 273.15) * 9/5 + 32

    else:
        print("Invalid unit conversion!")
        return

    print(f"Converted temperature: {result:.2f}°{convert_to}")

while True:
    print("===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Length Converter!")
        length_converter()

    elif choice == "2":
        print("You selected Weight Converter!")
        weight_converter()

    elif choice == "3":
        print("You selected Temperature Converter!")
        temperature_converter()

    elif choice == "4":
        print("Thank you for using unit converter!")
        break

    else:
        print("Invalid choice")