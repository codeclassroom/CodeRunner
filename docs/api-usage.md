# API Usage

coderunner provides the following class constructors

### code(source, lang, output, inp, path)

* **Parameters** :
	- source : The Source Code
	- lang : The Programming Language
	- output : Expected Output of the Program
	- inp : Standard Input to the program (optional).
	- path : specify mode of input. Set this to `False` if you are not using file paths (optional)

**Demo**:
```python

import coderunner

source_code = "path-to/test_python.py"
language = "Python"
expected_output = "path-to/output.txt"
standard_input = "path-to/input.txt"

# use this if you have a standard input to Program
r = coderunner.code(source_code, language, expected_output, standard_input)

# otherwise
r = coderunner.code(source_code, language, expected_output)

# Use path=False if not using file paths
r = coderunner.code("Hello, World", language, "Hello, World", path=False)
```

**Pointers ✏**

- In a `Java` program the class name should always be ***`Main`***.<br>
- Currently supported languages :
	- C (gcc 7.2.0)
	- C++ (g++ 7.2.0)
	- Java (OpenJDK 8)
	- Python (3.6.0)
	- Bash (4.4)
- Languages should be specified as string like "C++", "Java" etc.


Methods available in class `code()`.

### 1. run()
**Parameters** : `None` <br>
**Return Type** : `None` <br>
**Description**: Submits the program on Judge0's server.<br>
**Demo**:
```python

r.run()

```

### 2. getStatus()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns submission status.<br>

- List of Statuses :
	- In Queue
	- Processing
	- Accepted
	- Wrong Answer
	- Time Limit Exceeded
	- Compilation Error
	- Runtime Error (SIGSEGV)
	- Runtime Error (SIGXFSZ)
	- Runtime Error (SIGFPE)
	- Runtime Error (SIGABRT)
	- Runtime Error (NZEC)
	- Runtime Error (Other)
	- Internal Error
	- Exec Format Error

**Demo**:
```python

status = r.getStatus()
# Accepted, Wrong Answet etc.
```

### 3. getError()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns any error occured during program execution.
**Demo**:
```python

error = r.getError()
"""
'Error :   File "main.py", line 2\n'
 '    print("Hello, "  name)\n'
 '                        ^\n'
 'SyntaxError: invalid syntax\n'
"""
```

### 4. getOutput()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns the standard output of the program.<br>
**Demo**:
```python

stdout = r.getOutput()
# 'Hello, World\n'
```

### 5. getMemory()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns the memory used by the program (in kilobytes).<br>
**Demo**:
```python

memory = r.getMemory()
# 3688
```

### 6. getTime()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns execution time of the program. <br>
**Demo**:
```python

time_consumed = r.getTime()
# 0.031 seconds
```

### 7. getExitCode()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns exit code of program. <br>
**Demo**:
```python

exit_code = r.getExitCode()
# 0 on Accepted and 1 on Run Time Error
```

### 8. getSubmissionDate()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns submission date/time of the program on Judge0's Server. <br>
**Demo**:
```python

sub_date = r.getSubmissionDate()
# 2019-11-11T13:27:15.909Z
```
