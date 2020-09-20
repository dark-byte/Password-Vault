from cryptography.fernet import Fernet
import json

ekey = open('ekey.txt', 'rb')
key = ekey.read()
cipher = Fernet(key)


with open('db.json', 'r') as f:
    db = json.load(f)


def main(site, username, password):
    pw = cipher.encrypt(bytes(password, 'utf-8'))
    db[site] = [username, str(pw)]
    print(db)
    with open('db.json', 'w') as outfile:
        json.dump(db, outfile)
    # read(site)

def read(site):
    username = db[site][0]
    pw = cipher.decrypt(eval(db[site][1]))
    print(username)
    print(pw.decode())
