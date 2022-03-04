import random 
import time
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
	length = int(input("Enter password length: "))
	random.shuffle(characters)		
	password = []
	for i in range(length):
		password.append(random.choice(characters))	
	random.shuffle(password)
	print("".join(password))
generate_random_password()

"""def get_random_string(length):
    
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
 
    print(result_str)


get_random_string(8)
get_random_string(8)"""