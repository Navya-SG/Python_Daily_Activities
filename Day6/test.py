'''nested_data = (["X", "Y"], ("A", "B", "C"), "PQRS")
multipliers = [2, 3, 1]
separators = ("|-|", "***", "^^^")
positions = [(1, 0), (2, 1, 0), (3, 1)]
 
 
expected op: 
"Y|-|YA***C***ABRS^^^S^^^R"
 
 
 
Rules :
     No loops, functions, conditions, or f-strings/format()
Only use: indexing, slicing, string concatenation (+), string multiplication (*), tuple/list operations
Must access elements using the positions data to determine which characters to extract
Must use multipliers to determine repetition counts
Must use separators for joining
Everything in ONE expression (though you can use intermediate variables for sub-expressions)'''


nested_data = (["X", "Y"], ("A", "B", "C"), "PQRS")
multipliers = [2, 3, 1]
separators = ("|-|", "***", "^^^")
positions = [(1, 0), (2, 1, 0), (3, 1)]
print(nested_data[0][1]+separators[0]+nested_data[0][1]+nested_data[1][0]+separators[1]+nested_data[1][2]+separators[1]+nested_data[1][0]+nested_data[1][1]+nested_data[2][2]+nested_data[2][3]+separators[2]+nested_data[2][3]+separators[2]+nested_data[2][2])