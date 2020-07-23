from coderunner import coderunner
import os

from dotenv import load_dotenv
load_dotenv()

source_code = "testfiles/" + "test_python_input.py"
language = "Python3"
output = "testfiles/output/" + "output2.txt"
Input = "testfiles/input/" + "input.txt"

API_KEY = os.environ["API_KEY"]

r = coderunner.code(source_code, language, output, Input)

# Necessary step to initialize API keys & URL
r.api(key=API_KEY)

# run the code
r.run()

print("Running r :")
print("Status : " + r.getStatus())
print("Output : " + r.getOutput())
