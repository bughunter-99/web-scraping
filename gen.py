from random import randint, choice


def getUUID(length=10):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    randomlist = alphabet + numbers
    uuid = ''
    for i in range(length):
        uuid += str(choice(randomlist))
    return uuid
