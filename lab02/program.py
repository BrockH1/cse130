# 1. Name:
#      Brock Hoskins
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is meant to rectrieve a username and password from the user and authenticate the user.
# 4. What was the hardest part? Be as specific as possible.
#      Writing the right code to read the json file. I'm a little unfamiliar with the syntax involving reading and writing in files. The rest came to me pretty easily.
# 5. How long did it take for you to complete the assignment?
#      About 2 hours.



# Importing json.
import json

# Reading the json file.
try:
   with open("lab02.json", "r") as file:
      text2 = file.read()
      data2 = json.loads(text2)
except:
   print("Unable to open file Lab02.json.")
   quit

# Declaring the needed variables.
found_username = False

found_password = False

password_list = []

username_list = []

# Adding the data from the json object onto two separate lists.
for x in data2["username"]:
   username_list.append(x)

for x in data2["password"]:
   password_list.append(x)  

# Prompting the user for a username.
username = input("Username: ")

# Cheking to see if the user's inputed username exists in the list.
for x in username_list:
   if username == x:
      found_username = True

# Prompting the user for a passowrd.
password = input("Password: ")

# Checking to see if the user's inputed password exists in the list.
for x in password_list:
   if password == x:
      found_password = True

# If the password and or username doesn't exist, the user will not be authenticated.
if found_password is False or found_username is False:
   print("You are not authorized to use the system.")

# If the password and username have the same index number, the user will be authenticated.
else:
   if password_list.index(password) == username_list.index(username):
      print('You are authenticated!')
   else:
      print("You are not authorized to use the system.")

