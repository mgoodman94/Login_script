# Login Script
Python login script. Allows users to register an account, or log in to an existing account. Part 1 uses a config file with JSON formatting to store information. Part 2 uses sqlite3 to store information.

## Getting Started
### Part 1
  - <i>Script</i>: login_hashed.py
  - Asks user to either 'register' or 'login'.
  - If 'register' is selected: 
    - user will be asked to create a username and password.
    - config file will be scanned to ensure username is not already taken.
    - user password is hashed with sha256 hashing.
    - user account information is appended to config file in JSON format
  - If 'login' is selected:
    - user will be asked to enter their username and password.
    - password is hashed with sha256 hashing.
    - if username and hashed password match an existing account, return True
    
### Part 2
  - <i>Script</i>: login_sql.py
  - If SQL database does not exist, one will be created.
  - If SQL table for username and password does not exist, one will be created.
  - Asks user to either 'register' or 'login'.
  - If 'register' is selected: 
    - user will be asked to create a username and password.
    - SQL database will be scanned to ensure username is not already taken.
    - user password is hashed with sha256 hashing.
    - user account information is added to SQL table.
  - If 'login' is selected:
    - user will be asked to enter their username and password.
    - password is hashed with sha256 hashing.
    - if username and hashed password match an existing account in the SQL table, welcome the user.
    
## Author
  - Matthew H Goodman
  
## Acknowledgments 
  - Robert Heaton for the project idea and guidance.
