'''codes = ["1032","3X82","929@","0x00","--","0000","235%","8362"]
for code in codes:
	for char in code:
		if char.isdigit() and char.count("0") == 3 or char.count("0") == 4:
			print(char)
			break
		if not char.isdigit():
			continue

	
codes = ["1032","3X82","929@","0x00","--","0000","235%","836A"]
for code in codes:
	if code.isdigit():
		for char in code: 
			if char == "0":	
								break
		elif :
			break'''

codes = ["1032", "3X82", "929@", "0x00", "--", "0000", "235%", "836A", "000"]
for code in codes:
    if not code.isdigit():
        continue
    if code.isdigit():
        for char in code:
            if char == "0" and code.count("0") == 4 or code.count("0") == 3 :
                print(code)
                break
    
#final sol
codes = ["1032", "3X82", "929@", "0x00", "--", "0000", "235%", "836A", "000"]
for code in codes:
    if code.isdigit():
        for char in code:
            if char == "0" and code.count("0") == 4 or code.count("0") == 3 :
                print(code)
                break
    else:
        continue

#alter soln  
codes = ["1032", "3X82", "929@", "0x00", "--", "0000", "235%", "836A"]
for code in codes:
    if code.isdigit() and code.count("0") == 4 :
          print(code)
          break


