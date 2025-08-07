with open("original.txt","r") as infile:
    lines=infile.readlines()
reversed_lines = lines[::-1]
with open("reversed.txt","w") as outfile:
    outfile.writelines(reversed_lines)