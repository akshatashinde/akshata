import re

def validate_mobile(value):
    """ Raise a ValidationError if the value looks like a mobile telephone number.
    """
    rule = re.compile(r'/^[0-9]{10,14}$/')

    if not rule.search(value):
        msg ="Invalid mobile number."
        raise ValidationError(msg)
   
        #print "this is correct mobile no."    
        
validate_mobile("9422242204")        
