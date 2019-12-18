import unittest
from coderunner import coderunner

# test for Java program


class TestRunA(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_java.java"
        language = "Java"
        output = "testfiles/output/" + "output.txt"
        r = coderunner.code(source_code, language, output)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")

# test for Java program with input


class TestRunB(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_java_input.java"
        language = "Java"
        output = "testfiles/output/" + "output5.txt"
        Input = "testfiles/input/" + "input4.txt"
        r = coderunner.code(source_code, language, output, Input)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")

# test for Python program


class TestRunC(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_python.py"
        language = "Python"
        output = "testfiles/output/" + "output6.txt"
        r = coderunner.code(source_code, language, output)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")

# test for Python program with input


class TestRunD(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_python_input.py"
        language = "Python"
        output = "testfiles/output/" + "output2.txt"
        Input = "testfiles/input/" + "input.txt"
        r = coderunner.code(source_code, language, output, Input)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")


# test for C program


class TestRunE(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_c.c"
        language = "C"
        output = "testfiles/output/" + "output7.txt"
        r = coderunner.code(source_code, language, output)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")


# test for C program with input


class TestRunF(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_c_input.c"
        language = "C"
        output = "testfiles/output/" + "output3.txt"
        Input = "testfiles/input/" + "input2.txt"
        r = coderunner.code(source_code, language, output, Input)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")

# test for C++ program


class TestRunG(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_c++.cpp"
        language = "C++"
        output = "testfiles/output/" + "output8.txt"
        r = coderunner.code(source_code, language, output)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")


# test for C++ program with input


class TestRunH(unittest.TestCase):

    def test_run(self):
        source_code = "testfiles/" + "test_c++_input.cpp"
        language = "C++"
        output = "testfiles/output/" + "output4.txt"
        Input = "testfiles/input/" + "input3.txt"
        r = coderunner.code(source_code, language, output, Input)
        r.run()
        self.assertEqual(r.getStatus(),
                         "Accepted", "Something Wrong")


if __name__ == '__main__':
    unittest.main()
