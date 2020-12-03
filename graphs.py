
import random
from math import sqrt

def get_next_letter():
    current = 0
    while current < 26:
        yield chr(ord('a') + current)
        current += 1


class point:
    def __init__(self, letter) -> None:
        self.x
        self.y
        self.z
        self.node = letter

        self.create_random()
        
    def create_random(self, Xran=(-100,100), Yran=(-100,100), Zran=(-50,50)):
        self.x = random.uniform(Xran[0], Xran[1])
        self.y = random.uniform(Yran[0], Yran[1])
        self.z = random.uniform(Zran[0], Zran[1])

    def calculate_distance_to(self, other_point):
        return sqrt((self.x - other_point.x )**2 +(self.y - other_point.y)**2 +(self.z - other_point.z )**2 )

# letter = get_next_letter()
# print(next(letter))
# print(next(letter))
# print(next(letter))
# for let in get_next_letter():
#     print(let)