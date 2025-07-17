input=["Track A","Track B","Track C","Track D"]
input.pop(2)
input.remove("Track D")
input.insert(0,"Track X")
input.insert(1,"Track D")
print(*input)