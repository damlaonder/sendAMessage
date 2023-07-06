


# function: valid_username
# input: a username (string)
# valid username: (1) must be 5 characters or longer
#(2) must be alphanumeric (only letters or numbers)
#(3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)


def valid_username(x):
    #1: must be 5 characters or longer
    if len(x)<5:
        return False
    #3: first character cannot be a number
    elif ord(x[0])>= 48 and ord(x[0])<=57:
        return False
    #2: must be alphanumeric only
    for c in x:
        if ord(c) < 48 or ord(c)>57 and ord(c) <65 or ord(c)>90 and ord(c)<97 or ord(c)>122:
            return False
    else:
        return True


# function: valid_password
# input: a password (string)
# valid password:
#(1) must be 5 characters or longer
#(2) must be alphanumeric (only letters or numbers)
#(3) must contain at least one lowercase letter
#(4) must contain at least one uppercase letter
#(5) must contain at least one number
# output:     boolean (True if valid, False if invalid)

def valid_password(y):
    #identify what makes it invalid 
    #1: must be 5 characters or longer
    if len(y)<5:
        return False
    #3: must contain at least one lower case letter
    if not any(char.islower() for char in y):
        return False 
    #4: must contain at least one upper letter
    if not any(char.isupper() for char in y):
        return False
    #5: must contain at least one number
    if not any(char.isdigit() for char in y):
        return False
    #2: must be alphanumeric
    for c in y:
        if ord(c) < 48 or ord(c)>57 and ord(c) <65 or ord(c)>90 and ord(c)<97 or ord(c)>122:
            return False
   
    #true
    else:
        return True


# function: username_exists
# input: a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:boolean (True if found, False if not found)

def username_exists(x):   
    #open file
    file = open("user_info.txt", "r")
    data = file.read()
    file.close()

    data_list = data.split("\n")
    #start list of usernames
    usernames=[]
        #look at each string and divide into username and password
    for item in data_list:
        item_list = item.split(",")
    
        #for item in
        username = item_list[0]
        #add each username to the list 
        usernames.append(username)
    
    #determine if the username is in the list 
    if x in usernames:
        return True
    else:
        return False
        

    
# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)


def check_password(x, y):   
    #open file
    #hard coded!!!
    file = open("user_info.txt", "r")
    data = file.read()
    file.close()

    data_list = data.split("\n")
    #make a dictionary
    combos = {}
    

    #look at each string and divide into username and password
    for item in data_list:
        item_list = item.split(",")
        username = item_list[0]
        password = item_list[-1]
        # add pair to dictionary
        combos[item_list[0]] = item_list[-1]
    #determine if the passwords matches username combination 
    if (x, y) in combos.items():
        return True
    else:
        return False


# function: add_user
# input: a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#'user_info.txt' file they should be added, along with
# their password.
# output:     boolean (True if added successfully, False if not)

def add_user(username, password):
    file = open("user_info.txt","r")
    data = file.read()
    #parse this info from the file 
    data_list = data.split("\n")

    users = {}
    #look at each string, divide into username and password
    for item in data_list:

        item_list = item.split(",")

        # add pair to dictionary
        users[item_list[0]] = item_list[-1]

    #print(users)

    #add to file if not already listed
    if username not in users.keys():
        file = open("user_info.txt","a")
        file.write(username+","+password+"\n")
        send_message("admin", username, "Welcome to your account!")
        return
    else:
        return False 
  


# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the corresponding messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
# output:     nothing

import datetime
d = datetime.datetime.now()
month = d.month
day = d.day
year = d.year
hour = d.hour
minutes = d.minute
second = d.second
    
def send_message(sender, recipient, message):
    file = open(recipient, "a")
    time = str(month)+"/"+str(day)+"/"+str(year)+" "+ str(hour)+":"+str(minutes)+":"+str(second)
    file.write(sender+"|"+time+"|"+message+"\n")
    return ("Message Sent!")
    


# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.
#assume file is named 'name.txt':
# output:     no return value (simply prints the messages)


def print_messages(un):
    file = open(un, "r")
    data = file.read()
    
  
    #put message info info a list
    data_list = data.split("\n")
    #separate each message
    for item in data_list:
        item_list = item.split("|")
         #set up output/display
        try:
            print("Message #", "received from", item_list[0])
            print("Time: ", item_list[1])
            print(item_list[2])
            print()
        except:
            continue 






# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value


def delete_messages(username):
    file = open(username, "w").close()



#part f

choice = input("(l)ogin, (r)egister or (q)uit: ")

while choice != "q":
    if choice == "r":
        print()
        print("Register for an account")
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")

        #validate username and passwrod
        if valid_username(username) == False:
            print("Username is invalid, registration cancelled")
            print()
        elif valid_password(password) == False:
            print("Password is invalid, registration cancelled")
            print()

        if valid_username(username) == True and valid_password(password) == True:
            if username_exists(username) == True:
                print("Duplicate username, registration cancelled")
                print()
            elif username_exists(username) == False:
                add_user(username, password)
                print("Registration successful!")
                print()
       
        

    #choice = input("(l)ogin, (r)egister or (q)uit: ")
    print()
    #log in 
    if choice == "l":
        print("Log in")
        un = input("Username (case sensitive): ")
        pw = input("Password (case sensitive): ")
        
        #validate that username and password match
        if check_password(un, pw) == False:
            print("Invalid login")
        if check_password(un, pw) == True:
            print("You have been logged in successfully as", un)
            file = open(un, "a")
            #user choice
            userChoice = input("r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
            while userChoice!="l":
                if userChoice == "r":
                    print()
                    print_messages(un)
                    
                elif userChoice == "s":
                    print()
                    recipient = input("Username of recipient: ")
                    message = input("Type your message: ")
                    print(send_message(un, recipient, message))
                elif userChoice == "d":
                    delete_messages(un)
                print("You have been logged in successfully as", un)
                userChoice = input("r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
            if userChoice == "l":
                print("Logging out as username", un)
    
    choice = input("(l)ogin, (r)egister or (q)uit: ")
                         
                    

if choice == "q":
    print("Goodbye!")


