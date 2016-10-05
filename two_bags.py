# We have 2 opaque bags, each containing 2 balls.  One bag has 2 black balls and
# the  other  has  a  black  ball  and  a  white  ball.   You  pick  a  bag  at  random  and
# then pick one of the balls in that bag at random.  When you look at the ball,
# it  is  black.   You  now  pick  the  second  ball  from  that  same  bag.   What  is  the
# probability that this ball is also black?

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
