import sys
import py_compile
import optparse
import os
import random
import requests
from bs4 import BeautifulSoup


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

parser = optparse.OptionParser()
parser.add_option("--file", "-f", help="python file  ", action="store", dest="file")
parser.add_option("--output", "-o", help="output of python file ", dest="out", action="store")

option, arg = parser.parse_args()

payload = option.file

didi = open(payload, 'r')
hades = didi.read()
didi.close()

hd = open(payload, 'w')
while start != end:
    hd.write(random.choice(randomArray))
    start += 1
hd.close()

output = option.out
bytecode = option.out + "c"

try:
    py_compile.compile(payload, cfile=bytecode, dfile=None, doraise=False, )  # compilation
except (py_compile.PyCompileError, IOError, TypeError):
    sys.exit(IOError)
os.system("mv {}  {} ".format(bytecode, output))

