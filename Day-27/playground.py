def add(*args):
    addition = 0
    for num in args:
        addition += num
    return addition


print(add(1, 2, 4, 5, 5, 6))
