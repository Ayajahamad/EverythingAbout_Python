def validate_email(email):
    print()
    if email.count('@') != 1:
        return "Invalid Email: Must contain exactly one '@'."

    if not email[0].isalpha():
        return "Invalid Email: Must start with alphabet."

    if ' ' in email:
        return "Invalid Email: Email cannot contain spaces."
    
    if '..' in email:
        return "Invalid Email: Email not contain consecutive dot (..)"
    
    dissalowed_char = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '{', '}', '|', '<', '>', '?', '/', ':', ';', '"', "'", '\\', ',', ' ']
    for c in dissalowed_char:
        if c in email:
            return "Invalid Email: Special characters like [!#$%^&*()=+{}|<>?/:;\'\\,] are not allowed"

    if not email[-1].isalpha():
        return "Invalid Email: Email must ends with alphabet"
    
    username, domain = email.split('@')
    # print('domain: ',domain)
    if len(domain) < 3:
        return "Invalid Email: Email domain conatin minimum 2 character."
    
    if username.endswith('.'):
        return "Invalid Email: Email username not ends with (.)."
    
    if '.' not in domain:
        return "Invalid Email: Domain must contain a dot (.) after '@'."
    
    if not username or not domain:
        return "Invalid Email: Username and domain cannot be empty."

    return "Valid Email"

# Test cases
print(validate_email("user@example.com"))        
print(validate_email("user@domain.com@"))        
print(validate_email("user example@domain.com")) 
print(validate_email("user@domaincom"))         
print(validate_email("user@.com")) 
print(validate_email("123user@.com"))
print(validate_email("user@.c"))
print(validate_email("user@..com"))
print(validate_email("us$er@.com"))
print(validate_email("username@domain."))





