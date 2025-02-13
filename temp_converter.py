def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) *5/9

def celsius_to_kelvin(celsius):
  return (celsius + 273.15)

def kelvin_to_celsius(kelvin):
  return (kelvin - 273.15)

def menu():
  print(" ")
  print("Temperature Converter")
  print(" ")
  print("1. Celsius to Fahrenheit")
  print("2. Fahrenheit to Celsius")
  print("3. Celsius to Kelvin")
  print("4. Kelvin to Celsius")
  print("5. QUIT")
  print(" ")

  choice = eval(input("Choose your option (1-5): "))

  return choice

def main():
    while True:
      choice = menu()

      if choice == 1:
          try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
          except ValueError: 
            print("Invalid, Please enter a number.")

      elif choice == 2:
          try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
          except ValueError: 
            print("Invalid, Please enter a number.")

      elif choice == 3:
          try:
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is {kelvin:.2f}K")
          except ValueError: 
            print("Invalid, Please enter a number.")

      elif choice == 4:
          try:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K is {celsius:.2f}°C")
          except ValueError: 
            print("Invalid, Please enter a number.")
      
      elif choice == 5:
            print("BYE BYE BYE!!!")
            break

      else:

            print("Invalid choice. Try again")
