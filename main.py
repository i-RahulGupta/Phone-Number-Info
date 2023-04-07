import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with Country code: ")
mobileNo = phonenumbers.parse(mobileNo)

# Getting Time Zone of the number 
print(timezone.time_zones_for_number(mobileNo))

# Getting Carrier of the number
print(carrier.name_for_number(mobileNo, "en"))

# Getting Region Information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating a Phone Number
print("Valid Mobile Number :",phonenumbers.is_valid_number(mobileNo))

# Checking Possibility of the number
print("Checking possibility of Number :",phonenumbers.is_possible_number(mobileNo))
