#MATH
from math import pi,sqrt
print(sqrt(pi))

#square root
import math
print(math.sqrt(16))

#pi
import math
print(math.pi)

#ceil
import math
print(math.ceil(16.3))

#floor
import math
print(math.floor(16.3))

#power
import math
print(math.pow(4,2))

#activity
import math
pi=math.pi
r = 10
print("diameter:",2*r)
print("circumference:",2*pi*r) 
print("a:",pi*math.pow(r,2))


#RANDOM
#random.random() - random bt (0.0-1.0)
import random
print(random.random())

#random.random() - random integer bt (x,y)
import random
print(random.randint(2,9))

#random.choice(sequence) - random from given seq
import random
lst=[6,4,8,2,7,4,9]
print(random.choice(lst))

#random.shuffle(mutable seq-[list]) - shuffles the list randomly and return shuffled list
import random
lst=[6,4,8,2,7,4,9]
random.shuffle(lst)
print(lst)

#activity1
import random
def flip_biased_coin():
    return "Heads" if random.random() < 0.7 else "Tails"
print(flip_biased_coin())

#activity2
import random
participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]
givers = participants[:]
receivers = participants[:]
while True: # Keep shuffling until no one is assigned to themselves
    random.shuffle(receivers)
    if all(g != r for g, r in zip(givers, receivers)):
        break
for giver, receiver in zip(givers, receivers):
    print(f"{giver} -> {receiver}")# Print the pairings
