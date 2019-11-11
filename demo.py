from coderunner import coderunner
import pprint

program_name = "testfiles/" + "test_python.py"
language = "Python"
output = "testfiles/" + "output2.txt"
Input = "testfiles/" + "input.txt"
r = coderunner.Run(program_name, language, output, Input)

print("Status : " + r.getStatus())
if r.getError() != None:
	pprint.pprint("Error : " + r.getError())
else:
	print("Standard Output : ")
	pprint.pprint(r.getOutput())
print("Execution Time : " + r.getTime())
print("Memory : " + str(r.getMemory()))