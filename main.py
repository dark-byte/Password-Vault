from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

cipher = Fernet(key)

text = cipher.encrypt(b'This is encrypted')
print(text)

original_text = cipher.decrypt(text)
print(original_text.decode())

db = {}

def main(site, username, password):
    pw = cipher.encrypt(bytes(password, 'utf-8'))
    db[site] = [username, pw]
    read(site)

def read(site):
    username = db[site][0]
    pw = cipher.decrypt(db[site][1])
    print(username)
    print(pw.decode())

if __name__ == "__main__":
    main("instagram", "dark-byte", "password")