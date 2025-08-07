import random
participants=["Michael","Jim","Pam","Dwight","Angela"]
while True:
    dup_part=list(participants)
    random.shuffle(dup_part)
    if all(x!= dup_part for x,dup_part in zip(participants,dup_part)):
        break
for x,dup_part in zip(participants,dup_part):
    print(f"{x} -> {dup_part}")