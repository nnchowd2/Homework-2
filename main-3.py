def exact_change(user_total):
    numdollars = user_total // 100
    user_total %= 100
    numquarters = user_total // 25
    user_total %= 25
    numdimes = user_total // 10
    user_total %= 10
    numnickels = user_total // 5
    user_total %= 5
    numpennies = user_total // 1
    user_total %= 1
    return numdollars, numquarters, numdimes, numnickels, numpennies

if __name__ == "__main__":
    user_total = int(input())
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(user_total)

    if user_total <= 0:
        print("no change")
    else:
        if numdollars == 1:
            print(numdollars, "dollar")
        elif numdollars > 1:
            print(numdollars, "dollars")
        if numquarters == 1:
            print(numquarters, "quarter")
        elif numquarters > 1:
            print(numquarters, "quarters")
        if numdimes == 1:
            print(numdimes, "dime")
        elif numdimes > 1:
            print(numdimes, "dimes")
        if numnickels == 1:
            print(numnickels, "nickel")
        elif numnickels > 1:
            print(numnickels, "nickels")
        if numpennies == 1:
            print(numpennies, "penny")
        elif numpennies > 1:
            print(numpennies, "pennies")


