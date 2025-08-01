from re import M
from cryptography.fernet import Fernet
import os


def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)


def load_key():
    if not os.path.exists("key.key"):
        write_key()
    return open("key.key","rb").read()


master_pwd=input("Enter is the master password?: ")
key=load_key()
fer=Fernet(key)

def view():
    name=input("Enter the account name: ")
    with open("pass.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            if user==name:
                print(f"User: {user}, Password: {fer.decrypt(passw.encode('latin-1')).decode()}")
                return
            
    print("Account not found")
        

def add():
    name=input("Enter the account name: ")
    pwd=input("Enter the password: ")
    with open("pass.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode('latin-1')}\n")

while True:
    mode=input("Add new password or view existing passwords? (add/view): ")
    if mode=="view":
        view()
    elif mode=="add":
        add()
    elif mode=="quit":
        break
    else:
         print("Invalid mode")
         continue
        
