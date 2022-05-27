from Crypto.Cipher import PKCS1_OAEP


def encrypt_message(message: str, public_key) -> bytes:
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message.encode('utf-8'))


def decrypt_message(encrypted_message: bytes, private_key) -> str:
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_message).decode('utf-8')
