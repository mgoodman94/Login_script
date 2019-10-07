import hashlib
import json
import os

path = "C:/Users/16102/Documents/Advanced Beginner Projects/login"
os.chdir(path)


def sha_encrypt(pw):
    encode_hash = hashlib.sha256(pw.encode())
    hash_pw = encode_hash.hexdigest() 
    
    return hash_pw


def register(db):  
    # ensure username isn't already taken and passwords match       
    invalid = True
    while invalid:
        username = input("Please enter a username: ").lower()
        pw = input("Please enter a password: ")
        pw2 = input("Please confirm your password: ")
        
        if pw == pw2 and username not in db:
            invalid = False
        elif pw != pw2:
            print("Passwords are not the same")
        elif username in db:
            print("Username already taken")
            
    # hash password
    hash_pw = sha_encrypt(pw)
            
    # save to json database
    login_info = {username: hash_pw}
    db.update(login_info)
    with open("logins.json", 'w') as f:
        json.dump(db, f)
    
    
def is_valid_credentials(db):
    # get username and password and check if they match db users
    username = input("Please enter a username: ")
    pw = input("Please enter a password: ")
    
    return username.lower() in db and db[username.lower()] == sha_encrypt(pw)

    
def main():  
    # json database {username: password}
    if os.path.exists("logins.json"):
        with open("logins.json") as infile:
            database = json.load(infile)
    else:
        with open("logins.json", "w") as f:
            json.dump({}, f) 
        with open("logins.json") as infile:
            database = json.load(infile) 
            
    # ask to register or login
    undecided = True
    while undecided:
        log_type = input("Would you like to register or login? Type register or login: ")
        if log_type.strip().lower() == "register":
            register(database)
            break
        elif log_type.strip().lower() == "login":
            is_valid_credentials(database)
            break
        else:
            print("Please type a valid response")

    
main()
