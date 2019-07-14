import unittest
from judge import run

class TestRun(unittest.TestCase):
	def test_run(self):
		program_name = "testfiles/" + "test_java.java"
		language = "Java"
		output = "testfiles/" + "output.txt"
		self.assertEqual(run(program_name, language, output),
                     "Accepted", "Something Wrong")

if __name__ == '__main__':
    unittest.main()
