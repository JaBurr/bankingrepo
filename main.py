import os
import mysql.connector

 

connection = mysql.connector.connect(
    user = "root", 
    database = "example", 
    password = "mewhen"
)



cursor = connection.cursor()
 
account = None

#testQuery = ("SELECT * FROM bank")

 

#cursor.execute(testQuery)

 

#for item in cursor:

    #print(item)




#IMPORTANT FUNCTIONS!!!!!!!!!
def createAccount(fname, lname, email, addr, psw, bal): #Create an account.
    addData = ("INSERT INTO bank (firstName, lastName, email, balance, homeAddress, password) VALUES (%s, %s, %s, %s, %s, %s)")
    values = (
        fname,
        lname, 
        email,
        bal,
        addr,
        psw
    )

    cursor.execute(addData, values)
    connection.commit()

def checkBalance(): #Checks your balance.
    os.system("cls")
    cursor.execute(f"SELECT balance FROM bank WHERE id = {account[0]}")
    queryData = cursor.fetchone()
    return queryData[0]

def deposit(amt): #Deposit an amount.
    os.system("cls")
    #Save SQL table/data/row.
    #Tell user it has been deposited.
    cursor.execute(f"UPDATE bank SET balance = balance + {amt} WHERE id = '{account[0]}'")
    connection.commit()
    print(f"You have deposited ${amt} successfully into your account.\n\n")

def withdraw(amt): #Withdraw an amount.
    os.system("cls")
    #AMOUNT WITHDRAWING CANNOT EXCEED BALANCE!!!!!.
    #If it doesn't then:.
    #Subtract from the amount in SQL table.
    #Save SQL table.
    #Tell user it has been withdrawn.
    cursor.execute(f"SELECT balance FROM bank WHERE id = '{account[0]}'")
    balance = cursor.fetchone()
    if (balance[0] < amt):
        print("You do not have enough funds to perform this action.\n\n")
        return
    
    cursor.execute(f"UPDATE bank SET balance = balance - {amt} WHERE id = '{account[0]}'")
    connection.commit()
    print(f"You have withdrew ${amt} successfully from your account.\n\n")

def accountDetails():
    os.system("cls")
    print(f"First Name: {account[1]}\nLast Name: {account[2]}\nEmail: {account[3]}\nHome Address: {account[5]}\n\n")




os.system("cls") #clear up beginning gunk

#user interaction loop.
while True:

    response = int(input("Hello! What would you like to do today?\n\n(1) Login\n(2) Sign Up\n"))

    if response == 1: #Login
        email = input("Please enter your email address: ")
        psw = input("Please enter your password: ")

        #Check if account exists, if not, return to the beginning.
        cursor.execute(f"SELECT * FROM bank WHERE email = '{email}' AND password = '{psw}'")
        user = cursor.fetchone()
        if (user != None):
            account = user
            break
        os.system("cls")
        print("Incorrect Credentials. Please Try Again.\n")
    elif response == 2: #Signup
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        addr = input("Please enter your home address: ")
        psw = input("Please enter a password: ")
        bal = input("Please indicate a starting balance: ")
        createAccount(fname, lname, email, addr, psw, bal)
        cursor.execute(f"SELECT * FROM bank WHERE email = '{email}' AND password = '{psw}'")
        user = cursor.fetchone()
    else:
        os.system("cls")

os.system("cls") #clean up time

while True:
    response = int(input("What would you like to do?\n\n(1) View Account Details\n(2) Check Balance\n(3) Make A Deposit\n(4) Make A Withdrawal\n(5) Log Out"))

    if response == 1:
        #account details
        accountDetails()
    elif response == 2:
        #check balance
        print(f"You have ${checkBalance()} in your account.\n\n")
    elif response == 3:
        #Deposit function
        amt = float(input("How much do you want to deposit?\n"))
        deposit(amt)
    elif response == 4:
        #Withdraw function
        amt = float(input("How much do you want to withdraw?\n"))
        withdraw(amt)
    elif response == 5:
        #log out
        print("Successfully Logged Out.")
        break
        
        















cursor.close()

connection.close()