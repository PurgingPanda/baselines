import random

for i in range(31):
    for j in range(3):
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        print(',({}, {}, {})'.format(r,g,b))
