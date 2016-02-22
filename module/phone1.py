import string
import re

RE_phone = re.compile("^[a-z0-9]{3}-[a-z0-9]{3}-[a-z0-9]{4}$")

map_in  = 'abcdefghijklmnprstuvwxyz'
map_out = '222333444555667778889999'
mapped = string.maketrans( map_in , map_out )


def main():
    while True:
        phone_number= raw_input('Please enter a phone number in the format XXX-XXX-XXXX: ')
        phone_number = phone_number.lower()
        if RE_phone.match(phone_number):
            break
        print "Error. Please try again"
    print translateNumber(phone_number)

def translateNumber(phone_number):
    return phone_number.translate( mapped )

main()
