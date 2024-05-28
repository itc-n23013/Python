import re

def is_strong_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    
    if re.match(pattern, password):
        return '良いパスワードです' 
    else:
        return '大文字と小文字、１つ以上の数字を含んでください' 

passwords = [
    "Password123",
    "password123",
    "PASSWORD123",
    "Pass123",
    "Passw0rd",
    "StrongPass1"
]

for pwd in passwords:
    print(f"{pwd}: {is_strong_password(pwd)}")

