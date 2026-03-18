import re

##Validating email
def validate_email(email):
    
    ##The email must contain @ and .com should be at the end
    pattern = r"^[\w\.-]+@[\w\.-]+\.com$"
    
    match = re.fullmatch(pattern, email)
    if match:
        print("Valid")
    else:
        print("Invalid")


##Validating phone number
def validate_phone(phone):

    ## The number should start with 07 or 01 and have 10 numbers
    pattern = r"^(07|01)\d{8}$"

    match = re.fullmatch(pattern, phone)
    if match:
        print("Valid")
    else:
        print("Invalid")


##Validating password
def validate_password(password):

    ##The password must contain both letters and numbers and atleast 8 characters long
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

    match = re.fullmatch(pattern, password)
    if match:
        print("Valid")
    else:
        print("Invalid")

email_address = input("Enter email: ")
phone_number = input("Phone number: ")
user_password = input("Enter password: ")

validate_email(email_address)
validate_phone(phone_number)
validate_password(user_password)



