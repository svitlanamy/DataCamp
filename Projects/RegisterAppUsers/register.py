from python_functions import validate_name, validate_email, validate_password

def validate_user(name, email, password):
  #  print("validate_user")    

    if validate_name(name) == False:
        raise ValueError("Checks that the name is greater than two characters and is a string data type")
    if validate_email(email) == False:
        raise ValueError("Checks that the email address is in a valid format, has a username greater than 1 character, an '@' symbol, and an allowed domain that is in the `top_level_domains` variable")
    if validate_password(password) == False:
        raise ValueError("Checks that the password is strong enough. It should include a capital letter, a number between 0-9 and be greater than 8 characters")
    return True

def register_user(name, email, password):
    #print("register_user:") 
    try:
        validate_user(name, email, password)
    except:
      #print("An exception occurred")
      return False

    usr_dic = {'name': name, 'email': email, 'password': password}
    return usr_dic

# Call 
# register_user('Sveta', 'dfdfe@fh.com', 'dyukjhQ3fsdf')
# validate_user('John', 'john@example.com', 'securePassword123') 

