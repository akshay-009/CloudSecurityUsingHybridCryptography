import pickle
import sys
import getpass
import eel


def save_list(obj, name ):
    with open('Users/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_list(name):
    try:
        with open('Users/' + name + '.pkl', 'rb') as f:
          return pickle.load(f)
    except FileNotFoundError:
          return {}


users = load_list("list")

privilege = False
status = 0

if not users:
    accounts = 0
else:
    accounts = 1

@eel.expose
def newUser(createLogin, createPassword):   
    while True:
        
        if createLogin in users:
            print("\nLogin name already exist! Try again\n")
            break
        else:
            
            users[createLogin] = createPassword
  
            save_list(users, "list")
            print("\nUser created\n")
            break
 
@eel.expose
def login(login, password):
    global privilege
    global status
    count = 0
    while True:
   

        if login in users and users[login] == password and login == "admin":
            privilege = True
            status = 1
            print("\nLogin successful!\n")
            break
    
        elif login in users and users[login] == password:
            status = 1
            print("\nLogin successful!\n")
            break
 
        elif count == 3:
            print("\nToo many wrong tries. Goodbye!")
            break
        else:
           
            status = -1
            count = count+1
            print("\nUser doesn't exist or wrong password! Try again.\n")
            break

@eel.expose
def deleteUser(userName):
    
    if userName == "admin":
        print("Cannot delete the admin account.\n")
    elif userName in users:
  
        del users[userName]
        save_list(users, "list")
        print("User deleted.\n")

    else:
        print("User name does not exist in network.\n")

@eel.expose
def logOutPy():
    global privilege
    global status
    privilege = False
    status = 0