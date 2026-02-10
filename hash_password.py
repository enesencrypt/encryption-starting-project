import hashlib

password = "supersecret1453"

hashed = hashlib.sha256(password.encode()).hexdigest()

print("Password:", password)
print("Hashed:", hashed)
