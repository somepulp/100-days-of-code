import random

def random_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    random_color = (r,g,b)
    return random_color