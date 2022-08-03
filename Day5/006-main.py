for number in range(1,101):
    if number % 3 ==0 and number % 5 == 0:
        print(str(number) + " FizzBuzz")
    elif number % 3 == 0:
        print(str(number) + " Fizz")
    elif number %5 == 0:
        print(str(number) + " Buzz")
    else:
        print(str(number))