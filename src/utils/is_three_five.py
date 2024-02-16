def is_three_five(number: int):
    for num in range(1, number):
        if num % 3 == 0 and num % 5 == 0:
            print("ThreeFive")
        elif num % 3 == 0:
            print("Three")
        elif num % 5 == 0:
            print("Five")
        else:
            print(num)


is_three_five(101)
