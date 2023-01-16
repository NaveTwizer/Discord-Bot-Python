import random



def coin():
    return 'Heads' if random.randint(1, 2) == 1 else 'Tails'