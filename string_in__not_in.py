x = "Hello, Arindam"

print ("Ex1")
if "hello" in x:
    print ("Yes, the 'hello' keyword is present")
else:
    print ("No, the 'hello' keyword is not present")


print ("Ex2")
if "Hello" in x:
    print ("Yes, the 'Hello' keyword is present")
else:
    print ("No, the 'Hello' keyword is not present")

z = """
My phone number is
9836395513
and
My email address is
arindam.roy.developer@gmail.com
"""

print ("Ex3")
if "9836395513" in z:
    print ('Yes, the phone number is exist')
else:
    print ('No, the phone number is not found within the string')


print ("Ex4")
_findEmail = "arindam.roy.developer@gmail.com"
if _findEmail in z:
    print ('Yes, the email id is exist')
else:
    print ('No, the email id is not found within the string')


print ("Ex5")
_findEmail = "arindam.php@gmail.com"
if _findEmail in z:
    print ('Yes, the email id is exist')
else:
    print ('No, the email id is not found within the string')
