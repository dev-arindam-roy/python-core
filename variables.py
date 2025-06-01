"""
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myName = "Arindam Roy"
print (myName)

first_name = "Arindam"
last_name = "Roy"
print (first_name)
print (last_name)

emailId = 'arindam.roy.developer@gmail.com'
mobileNo = "+91-9836395513"

print (emailId, mobileNo)
print (emailId + mobileNo)
print ("Email Id is: " + emailId)
print ('Mobile No is: ' + mobileNo)
print ('Email: ' + emailId + ' and Mobile: ' + mobileNo)

_myProfession = "Developer / Programmer"
print (_myProfession)
