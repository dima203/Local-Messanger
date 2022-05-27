import unittest
from core.main import encrypt_message, decrypt_message
from Crypto.PublicKey import RSA


class CoreTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()
        self.message = "Hello, World!"

    def test_crypt(self) -> None:
        encrypted_message = encrypt_message(self.message, self.public_key)
        decrypted_message = decrypt_message(encrypted_message, self.private_key)
        assert self.message == decrypted_message


if __name__ == '__main__':
    unittest.main()
