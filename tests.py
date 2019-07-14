import unittest
from judge import run

class TestRunA(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_java.java"
		language = "Java"
		output = "testfiles/" + "output.txt"
		self.assertEqual(run(program_name, language, output),
                     "Accepted", "Something Wrong")


class TestRunB(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_python.py"
		language = "Python"
		output = "testfiles/" + "output2.txt"
		Input = "testfiles/" + "input.txt"
		self.assertEqual(run(program_name, language, output, Input),
                     "Accepted", "Something Wrong")


if __name__ == '__main__':
    unittest.main()
