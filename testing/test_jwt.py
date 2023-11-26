import unittest
from auth.jwt_handler import decode_jwt

class TestDecodeJWT(unittest.TestCase):
    def test_decode_jwt(self):
        print("test")
        print(decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHBpcmVzIjoxNzAwOTUwMDg5LjE5NTcyM30.ui_7SDtG1NKXQQAvLU4JS6ye87WkrA2MBlseS9ZSPI4"))

if __name__ == '__main__':
    unittest.main()