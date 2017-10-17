def countdown(start):
    if start > 0:
        print(start)
        countdown(start - 1)


# countdown(3)

def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


print(fact(5))
