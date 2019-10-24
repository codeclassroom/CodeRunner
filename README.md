# CodeRunner
> The future code runner for CodeClassroom (_WIP_)


### Installation
1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git https://github.com/codeclassroom/CodeRunner.git
```
3. Install Dependencies.
```bash
pip install -r requirements.txt
```
4. Run tests.
```bash
python3 tests.py
```

### Usage

```python
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
```


### Pointers ✏
- In a `Java` program the class name should always be ***`Main`***.
- Currently supported languages :
  - C (gcc 7.2.0)
  - C++ (g++ 7.2.0)
  - Java (OpenJDK 8)
  - Python (3.6.0)



### Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)
