def fizzbuzz(n):
    """
    Print FizzBuzz sequence from 1 to n.
    - Print "Fizz" for multiples of 3
    - Print "Buzz" for multiples of 5
    - Print "FizzBuzz" for multiples of both 3 and 5
    - Print the number otherwise
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(15)
