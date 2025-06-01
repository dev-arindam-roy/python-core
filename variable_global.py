x = "Arindam Roy"
print (x)

def myName():
    x = "Santanu Roy"
    print (x)

myName()
print (x)
print ("======================================")

z = "Hello Python"

def myFunc():
    #print (z)
    global z
    z = "Hello Arindam"
    print (z)
    
print (z)
myFunc()
print (z)
