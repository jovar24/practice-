def bonus_time(salary, bonus):
    if bonus == True:
        salary = salary * 10
        print(f"${salary}")
    elif bonus == False:
        salary = salary
        print(f"${salary}")


bonus_time(25000, True)


def apple(x):
    if int(x)**2 >= 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."


apple(50)


def is_digit(n):
    n = n.isnumeric()
    print(n)


is_digit("")
