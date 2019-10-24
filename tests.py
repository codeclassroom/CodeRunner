import unittest
from CodeRunner import run

#test for Java program
class TestRunA(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_java.java"
		language = "Java"
		output = "testfiles/" + "output.txt"
		r = run.coderunner(program_name, language, output)
		self.assertEqual(r.run(),
                     "Accepted", "Something Wrong")

#test for Python program
class TestRunB(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_python.py"
		language = "Python"
		output = "testfiles/" + "output2.txt"
		Input = "testfiles/" + "input.txt"
		r = run.coderunner(program_name, language, output, Input)
		self.assertEqual(r.run(),
                     "Accepted", "Something Wrong")

#test for C program
class TestRunC(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_c.c"
		language = "C"
		output = "testfiles/" + "output3.txt"
		Input = "testfiles/" + "input2.txt"
		r = run.coderunner(program_name, language, output, Input)
		self.assertEqual(r.run(),
                     "Accepted", "Something Wrong")

#test for C++ program
class TestRunD(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_c++.cpp"
		language = "C++"
		output = "testfiles/" + "output4.txt"
		Input = "testfiles/" + "input3.txt"
		r = run.coderunner(program_name, language, output, Input)
		self.assertEqual(r.run(),
                     "Accepted", "Something Wrong")


if __name__ == '__main__':
    unittest.main()
