#
sentence=input("Enter a sentence:")
vowels=["a","e","i","o","u"]
count=0
for char in sentence.lower():
    if char in vowels:
        count += 1
print("Number of vowels:",count)

#
print(sum(1 for char in input().lower() if char in ["a","e","i","o","u"]))



