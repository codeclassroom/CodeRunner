# Usage

coderunner provides the following class.

### code(source, lang, output, inp, path)

* **Parameters(type)** :
	- source : The Source Code
	- lang : The Programming Language
	- output : Expected Output of the Program (optional).
	- inp : Standard Input to the program (optional).
	- path : specify mode of input. Set this to `False` if you are not using file paths (optional)

**Demo**:
```python

from coderunner.coderunner import code

source_code = "path-to/test_python.py"
language = "Python3"
expected_output = "path-to/output.txt"
standard_input = "path-to/input.txt"

# use this if you have a standard input to Program
r = code(source_code, language, expected_output, standard_input)

# otherwise
r = code(source_code, language, expected_output)

# you can also ignore both fields
r = code(source_code, language)

# Use path=False if not using file paths
r = code("Hello, World", language, "Hello, World", path=False)
```

See [demo.py](https://github.com/codeclassroom/CodeRunner/blob/master/demo.py) for a more descriptive usage.

**Pointers ✏**

- In a `Java` program the class name should always be ***`Main`***.<br>
- CodeRunner supports all languages provided by Judge0. See full list of supported languages [here](https://jsonpp.judge0.com/?https://api.judge0.com/languages).
or you can use
```python
print(r.languages)
"""
['Assembly', 'Bash', 'Basic', 'C', 'C++', 'C#', 'Common Lisp', 'D', 'Elixir', 'Erlang', 'Executable', 'Fortran', 'Go', 'Haskell', 'Java', 'JavaScript', 'Lua', 'OCaml', 'Octave', 'Pascal', 'PHP', 'Plain Text', 'Prolog', 'Python2', 'Python3', 'Ruby', 'Rust', 'TypeScript']
"""
```
- Languages should be specified as string like "C++", "Java" etc.


Methods available in class `code()`.

### api()

Since v1.0, you need to provide a API Key & URL for using Judge0 through coderunner.

Here is an example on how to do this.

```python
from coderunner import coderunner
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

r.run()

print("Run r :")
print("Status : " + r.getStatus())
print("Output : " + r.getOutput())
````

The default API URL is [https://judge0.p.rapidapi.com/]()

### 1. run()
**Parameters(type)** : Number Of Runs (`int`), optional<br>
**Return Type** : None <br>
**Description**: Submits the program on Judge0's server.<br>
**Demo**:
```python

# by default the program executes 1 time on server.
r.run()

# to execute program 2 times, use
r.run(2)

```

### 2. getStatus()

**Parameters(type)** : None <br>
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

**Parameters(type)** : None <br>
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

**Parameters(type)** : None <br>
**Return Type** : `String` <br>
**Description**: Returns the standard output of the program.<br>
**Demo**:
```python

stdout = r.getOutput()
# 'Hello, World\n'
```

### 5. getMemory()

**Parameters(type)** : None <br>
**Return Type** : `String` <br>
**Description**: Returns the memory used by the program (in kilobytes).<br>
**Demo**:
```python

memory = r.getMemory()
# 3688
```

### 6. getTime()

**Parameters(type)** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns execution time of the program. <br>
**Demo**:
```python

time_consumed = r.getTime()
# 0.031 seconds
```

### 7. getExitCode()

**Parameters(type)** : None <br>
**Return Type** : `String` <br>
**Description**: Returns exit code of program. <br>
**Demo**:
```python

exit_code = r.getExitCode()
# 0 on Accepted and 1 on Run Time Error
```

### 8. getSubmissionDate()

**Parameters(type)** : None <br>
**Return Type** : `String` <br>
**Description**: Returns submission date/time of the program on Judge0's Server. <br>
**Demo**:
```python

sub_date = r.getSubmissionDate()
# 2019-11-11T13:27:15.909Z
```

### 9. setFlags(options)

**Parameters(type)** : Compiler flags (`String`) <br>
**Return Type** : `None` <br>
**Description**: Options for the compiler (i.e. compiler flags). <br>
**Demo**:
```python

r.setFlags("-O2 -Wall")

```

### 10. setArguments(arguments)

**Parameter Type** : Command line arguments (`String`) <br>
**Return Type** : `None` <br>
**Description**: Command line arguments for the program. <br>
**Demo**:
```python

r.setArguments()

```
