sentence="Python make you think differently".split()
print(sentence[1:-1])

sentence="Python make you think differently".split()
print(sentence[1],sentence[2],sentence[3])

sentence="Python make you think differently"
first, *middle, last = sentence.split()
print(middle)