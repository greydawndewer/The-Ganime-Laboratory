import random
from math import sqrt


def random_pi(num):
    if num <= 0:
        return "0 iteration value cant be given"

    pincir = 0
    pinsqa = 0
    for i in range(0, num):
      x = random.uniform(0, 1)
      y = random.uniform(0, 1)
      d = sqrt(x**2 + y**2)

      if d < 1:
          pincir += 1
      pinsqa += 1
    pi = (4*float(pincir))/float(pinsqa)
    return round(pi, 5)

pi = 0

while pi != 3.14159:
    pi = random_pi(1000000)
    print(pi)



