def oddOrEven(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def square(num):
    print("The square is", num * num)

def cube(num):
    print("The cube is", num * num * num)

def main():
    number = int(input("Enter a number: "))
    oddOrEven(number)
    square(number)
    cube(number)

main()

 

