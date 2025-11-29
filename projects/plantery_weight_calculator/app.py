# Constants on global scope
gravity_constants =  {

      "MERCURY" : 0.376,
       "MARS"    : 0.378,
      "VENUS " : 0.889,
      "JUPITER" : 0.2360,
      "SATURN"  : 0.1081,
      "URANUS"  : 0.815,
      "NEPTUNE" : 0.1140,
  }

# Weight Calculation

def weight_on_planets(earth_weight,planet):


  if planet.upper() in gravity_constants:
    calculate_weight_on_planets = earth_weight * gravity_constants[planet.upper()]
    return  f'Your weight on {planet.capitalize()} is {calculate_weight_on_planets :.2f} '
  else :
    return f'Invalid Planet Input'

# Better Practice for handling errors(Exception Handling)

def main():
  # Exception Handling for weight input
    while True :
      try :
        # prompt :
        earth_weight : float = float(input("Enter a weight on Earth: "))
        break
      except ValueError:
        print("Weight must be a number.")
   # Exceptio  Handling for plant input
    while True:
        planet : str = str(input("Enter a planet: "))
        result = weight_on_planets(earth_weight,planet)
        if result != 'Invalid Planet Input':
            print(result)
            break
        else:
            print(result)


main()