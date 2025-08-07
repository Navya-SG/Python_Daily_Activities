import random
def flip_biased_coin():
    return "Heads" if random.random() < 0.7 else "Tails"
print(flip_biased_coin())
    