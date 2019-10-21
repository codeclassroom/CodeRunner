import CodeRunner.run as cr

program_name = "testfiles/" + "test_python.py"
language = "Python"
output = "testfiles/" + "output2.txt"
Input = "testfiles/" + "input.txt"
r = cr.coderunner(program_name, language, output, Input)

print("Status : " + r.run())
if r.getError() != None:
	print("Error : " + r.getError())
else:
	print("stdout : " + r.getStandardOutput())
print("Execution Time : " + r.getTime())
print("Memory : " + str(r.getMemory()))