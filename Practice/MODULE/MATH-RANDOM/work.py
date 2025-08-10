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

