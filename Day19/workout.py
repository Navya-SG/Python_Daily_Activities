#
import datetime
print(datetime.datetime.now())

#
from datetime import time
t=time(10,45,30)
print(t)
print(t.hour,t.minute,t.second)

#
import datetime
print(datetime.MINYEAR(2))

#
from datetime import datetime
now=datetime.now()
print(now)

#
from datetime import datetime
now=datetime.now()
print(now)
print(f"{now.day}:{now.month}:{now.strftime("%y")}")

#
try:
    file = open('Day19\hello.txt','r')
    content = file.read()
    print(content)
    file.close()
except:
    print("File not found") #Hello, World

#
try:
    file = open('Day19\hello1.txt','r')
    content = file.read()
    print(content)
    file.close()
except:
    print("File not found") #File not found

#
try:
    file = open('Day19\hello1.txt','r')
    content = file.read()
    print(content)
    file.close()
except:
    print("File not found") #File not found

#
try:
    file1 = open('Day19\hello1.txt','r')
except:
    print("File not found") #File not found
else:
    content = file1.read()
    print(content)
finally:
    file1.close()

#
try:
    result = 10 / 0
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Error message:", e)
