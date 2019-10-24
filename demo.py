from CodeRunner import run
import pprint

program_name = "testfiles/" + "test_python.py"
language = "C#"
output = "testfiles/" + "output2.txt"
Input = "testfiles/" + "input.txt"
r = run.coderunner(program_name, language, output, Input)

print("Status : " + r.run())
if r.getError() != None:
	pprint.pprint("Error : " + r.getError())
else:
	print("Standard Output : ")
	pprint.pprint(r.getStandardOutput())
print("Execution Time : " + r.getTime())
print("Memory : " + str(r.getMemory()))