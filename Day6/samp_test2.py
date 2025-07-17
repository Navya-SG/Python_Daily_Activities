'''Take a string, remove all spaces, convert to uppercase, replace every 'A' with 'XXX', then extract characters at positions that are multiples of 3, and finally reverse the result.
 
input:
text = "amazing python language"
 
output:
"GNGXXXA"'''


text = "amazing python language"
remove = text.replace(" ","")
upper = remove.upper()
replace = upper.replace("A","XXX")
multiples = replace[::3]   #XXXMXXXZINGPYTHONLXXXNGUXXXGE
reverse = multiples[::-1]
print(reverse)