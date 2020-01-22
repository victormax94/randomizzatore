import sys
import py_compile
import optparse
import os
import random
import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet

def random_code_generation():
    url = "http://www.4geeks.de/cgi-bin/webgen.py"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    tagStart = '<pre>'
    tagEnd = '</pre>'
    code = str(soup.find('pre')).replace(tagStart, "").replace(tagEnd, "")
    print(str(code))
    return code


randomArray = [random_code_generation(), random_code_generation(), random_code_generation(), random_code_generation()]
_output_ = "backdoor.py"  # edit this line is you want edit default output .
_byte_ = (_output_) + "c"  # bytecode format

start = 1
end = random.randint(9, 20)


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key


parser = optparse.OptionParser()
parser.add_option("--file", "-f", help="python file  ", action="store", dest="file")
parser.add_option("--output", "-o", help="output of python file ", dest="out", action="store")

option, arg = parser.parse_args()

payload = option.file


hd = open(payload, 'w')


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open("criptato", "wb") as file:
            file.write(encrypted_data)


def decrypt(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open("decripted.py", "wb") as file:
        file.write(decrypted_data)

while start != end:
    hd.write(random.choice(randomArray))
    start += 1
hd.close()

output = option.out
bytecode = option.out + "c"


encrypt("payload.py", write_key())

decrypt("criptato", open("key.key").read())




try:
    py_compile.compile(payload, cfile=bytecode, dfile=None, doraise=False, )  # compilation
except (py_compile.PyCompileError, IOError, TypeError):
    sys.exit(IOError)
os.system("mv {}  {} ".format(bytecode, output))

