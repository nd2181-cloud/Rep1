#Nahomi Tesfaye Duki 
#ID: 433000292

def Triangle_validator(side1, side2, side3):
  if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    """validates if the three sides can form a triangle"""

    print("True")

    """prints True if the sides can form a triangle"""

  else:
    print("False")

    """prints False if the sides cannot form a triangle"""

#this function checks if the sides can form a triangle or not

def main():
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))
    """to take three inputs from the user"""
    Triangle_validator(side1, side2, side3)
    """calls the triangle validator function and passes the three inputs to it"""
main()
#this main function calls the triangle validator function and takes inputs from the user