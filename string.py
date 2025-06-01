_myStr1 = "Arindam Roy"
print (_myStr1)

_myStr2 = """
    Hello, Arindam
    How are you?
    What's going on....
    """
print (_myStr2)

_myStr3 = """
Hello
Arindam,
How Are
You.

Hey! I'm fine.
"""
print (_myStr3)

_myStr4 = "Arindam"
print (_myStr4[0], _myStr4[1])

_myStr5 = "Arindam"
for x in _myStr5:
    print (x)

_myStr6 = "Arindam"
print(len(_myStr6))

_myStr6 = "My name is Arindam Roy"
print ("is" in _myStr6)
print ("Mr." not in _myStr6)

if "is" in _myStr6:
    print ("Yes, 'is' keywork is present")
else:
    print ("No, 'is' keyword not present")
