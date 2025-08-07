#
from greetings import say_hello, say_bye
print(f"{say_hello('Abi')} {say_bye('Abi')}")

#
from greetings import say_hello as hello, say_bye as bye
print(hello('Abi'),bye('Abi'))
