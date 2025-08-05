def count_frequencies(nums):
    freq={}
    for num in nums:
        freq[num] = freq.get(num,0)+1
    return list(freq.items())
nums=[4,2,4,3,2]
print(count_frequencies(nums))
