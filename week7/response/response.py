import validators

address = input("What's your email address? ")
if validators.email(address):
    print("Valid")
else:
    print("Invalid")
