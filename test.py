import os
import hashlib
import logging
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

debug_file = "test.log"

logging.basicConfig(filename=debug_file, filemode='w', format='%(levelname)s: %(message)s', level=logging.INFO)
logging.info("This is a test log.")

for i in range(1000):
    logging.info("Test {}\n".format(i))

logging.shutdown()

with open(debug_file, "rb+") as f:
    data = f.read()
    hashed_password = hashlib.sha1("abcdef".encode()).digest()[:16]
    cipher = AES.new(hashed_password, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    f.seek(0)
    f.write(ct_bytes)
    f.truncate()
