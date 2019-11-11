# API Usage

coderunner provides the following class constructors

### Run(source, lang, output, inp)

* **Parameters** :
	- source : The Source Code
	- lang : The Programming Language
	- output : Expected Output of the Program
	- inp : Standard Input to the program (optional).
	- path : specify mode of input.Set this to `False` if you are not using file paths (optional)

**Demo**:
```python

import coderunner

program_name = "path-to/test_python.py"
language = "Python"
output = "path-to/output.txt"
Input = "path-to/input.txt"

# use this if you have a standard input to Program
r = coderunner.Run(program_name, language, output, Input)

# otherwise
r = coderunner.Run(program_name, language, output)

# if not using file paths
r = coderunner.Run("Hello, World", language, "Hello, World", path=False)
```

**Pointers ✏**

- In a `Java` program the class name should always be ***`Main`***.<br>
- Currently supported languages :
	- C (gcc 7.2.0)
	- C++ (g++ 7.2.0)
	- Java (OpenJDK 8)
	- Python (3.6.0)
- Languages should be specified as string like "C++", "Java" etc.


Methods available in class `Run()`.

### 1. getStatus()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Submits the program on Judge0's server and returns its status. Returns either `Accepted` or `Runtime Error (NZEC)`.<br>
**Demo**:
```python

r.getStatus()
# Accepted or Runtime Error (NZEC)
```

### 2. getError()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns any error occured during program execution.
**Demo**:
```python

r.getError()
# For e.g
"""
'Error :   File "main.py", line 2\n'
 '    print("Hello, "  name)\n'
 '                        ^\n'
 'SyntaxError: invalid syntax\n'
"""
```

### 3. getOutput()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns the standard output of the program.<br>
**Demo**:
```python

r.getOutput()
# For e.g 'Hello, World\n'
```

### 4. getMemory()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns the memory used by the program (in kilobytes).<br>
**Demo**:
```python

r.getMemory()
# For e.g 3688
```

### 5. getTime()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns execution time of the program. <br>
**Demo**:
```python

r.getTime()
# For e.g 0.031 seconds
```

### 6. getExitCode()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns exit code of program. <br>
**Demo**:
```python

r.getExitCode()
# For e.g 0 on Accepted and 1 on Run Time Error
```

### 7. getSubmissionDate()

**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns submission date/time of the program on Judge0's Server. <br>
**Demo**:
```python

r.getSubmissionDate()
# For e.g 2019-11-11T13:27:15.909Z
```
