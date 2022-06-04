import uuid
import cryptocode


def pwd_encrypt(key_encrypt):
    password_to_encrypt = f"{key_encrypt}|{uuid.uuid4()}"
    password_encrypt = cryptocode.encrypt(password_to_encrypt, key_encrypt)
    print(f"password_encrypt: {password_encrypt}")
    return password_encrypt

def pwd_decrypt(key_decrypt, encrypt_password):
    password_decrypt = cryptocode.decrypt(encrypt_password, key_decrypt)
    return password_decrypt
