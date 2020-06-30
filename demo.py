from coderunner import coderunner
import pprint
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

# r2 = coderunner.code("print(\"yo\")", "Python3", "YO", path=False)

# # run the code
r.run()

print("Run r :")
print("Status : " + r.getStatus())
print("Output : " + r.getOutput())

# r2.run()

# print("Run r2 :")
# print("Status : " + r2.getStatus())

# # check if any error occured
# if r.getError() is not None:
#     pprint.pprint("Error : " + r.getError())
# else:
#     print("Standard Output : ")
#     pprint.pprint(r.getOutput())
# print("Execution Time : " + r.getTime())
# print("Memory : " + str(r.getMemory()))
