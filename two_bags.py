import random

def random_bag():
    bags = [("b","w"), ("b", "b")]
    return random.choice(bags)

def random_ball(bag):
    if random.choice(bag) == "w":
        return None
    if bag == ("b","b"):
        return 1
    else: return 0
i = 0
a = 0
while i < 1000000:
    result = random_ball(random_bag())
    if result is not None:
        i += 1
        a += result
        P = a / float(i)
        print str(a) + ' e crnoto  ' + str(i) + ' dosegashni obidi.   Presmetana verojatnost:' + str(P)
