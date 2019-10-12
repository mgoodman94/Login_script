import hashlib
import os
import sqlite3
from getpass import getpass

def setup_db(cursor):
    # creates table in database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
        );
        ''')

def count_users(cursor):
    # count users and ask to recreate db
    count_users = '''SELECT * FROM users;'''
    c.execute(count_users)
    return len(c.fetchall())


def drop_user_table(cursor):
    cursor.execute("DROP TABLE users;")


def show_db():
    # displays all registered users
    c.execute('''SELECT * FROM users;''')
    rows = c.fetchall()
    
    for row in rows:
        print(row)   


def sh256(pw):
    # sha256 hashing
    encode_hash = hashlib.sha256(pw.encode())
    hash_pw = encode_hash.hexdigest() 
    
    return hash_pw


def register(c, username, pw)
    # hash password
    hash_pw = sh256(pw)
            
    # save to sqlite3 database. Return error if username taken
    try:
        c.execute(
            "INSERT INTO users VALUES (?, ?);"
            (username, hash_pw)
        )
        return True
    except sqlite3.IntegrityError:
        return False
    

def is_valid_credentials(cursor, username, pw):
    hash_pw = sh256(pw)
    
    # execute sqlite3 command. Returns None if doesn't exist
    cursor.execute(
         '''SELECT * FROM users WHERE username=? AND password=?;'''
         (username, hash_pw)
    )
    return cursor.fetchone() is not None

    
def main():
    path = "C:/Users/16102/Documents/Advanced Beginner Projects/login/Part 2_SQL"
    os.chdir(path)

    # connect to sqlite3
    conn = sqlite3.connect(os.path.join(path, "users_db.db"))
    c = conn.cursor()

    setup_db(c)

    num_users = count_users(c)
    print("Your users table currently holds %d users." % num_users)
    
    user_resp = input("Would you like to delete the current table and start over? (y/n): ")
    if user_resp.lower().strip() in ['y', 'yes']:
        drop_user_table(c)
        setup_db(c)
        
    # ask to register or login
    undecided = True
    while undecided:
        log_type = input("Would you like to register or login? Type register or login: ")
        if log_type.strip().lower() == "register":
            username = input("Please enter a username: ").lower()
            
            # ensure passwords match      
            while True:
                pw = getpass("Please enter a password: ")
                pw2 = getpass("Please confirm your password: ")
                
                if pw == pw2:
                    break
                else:
                    print("Passwords are not the same")

            success = register(c, username, pw)
            if success:
                print("Success!")
            else:
                print("ERROR: Username already exists")

            break
        elif log_type.strip().lower() == "login":
            # get username and password and check if they match db users
            username = input("Please enter a username: ")
            pw = getpass("Please enter a password: ")

            if is_valid_credentials(c, username, pw)
                print("Welcome")
            else:
                print("Login failed. Username or password is incorrect.")

            break
        else:
            print("Please type a valid response")

    # closing connection and commiting changes
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    main()