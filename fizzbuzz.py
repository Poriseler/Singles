for n in range(1,40):
    number = ""

    if n % 3 == 0:
        number += "Fizz"
    if n % 5 == 0:
        number += "Buzz"
    print(number or n)