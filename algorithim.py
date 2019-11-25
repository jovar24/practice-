def bonus_time(salary, bonus):
    if bonus == True:
        salary = salary * 10
        print(f"${salary}")
    elif bonus == False:
        salary = salary
        print(f"${salary}")


bonus_time(25000, True)
