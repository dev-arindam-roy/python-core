_myAge = 35
print (f"Hello, I'm A.Roy and My age is {_myAge}")

_gitRating = 4.5
_repoURL = "https://github.com/dev-arindam-roy"
_txtLine = f"My GIT URL is {_repoURL} and Rating is {_gitRating}"
print (_txtLine)


productName = "ONEX-CRM"
productPrice = 10.99
productRating = 3.9
productLine = f"{productName} - ${productPrice:.2f}/monthly. Rating is {productRating:.2f}"
print (productLine)


price = 59
tax = 0.25
txt = f"The price is {price + (price * tax):.2f} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
