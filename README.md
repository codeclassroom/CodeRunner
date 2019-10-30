# CodeRunner 🏃
> [Judge0 API](https://api.judge0.com/) Interface written in Python

[![GitHub license](https://img.shields.io/github/license/codeclassroom/CodeRunner)](https://github.com/codeclassroom/CodeRunner/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/codeclassroom/CodeRunner?color=blueviolet)](https://github.com/codeclassroom/CodeRunner/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](http://makeapullrequest.com)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/codeclassroom/CodeRunner?style=plastic)

### Prerequisites
1. Python 3.6+
2. virtualenv

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
from coderunner import coderunner
import pprint

program_name = "testfiles/" + "test_python.py"
language = "Python"
output = "testfiles/" + "output2.txt"
Input = "testfiles/" + "input.txt"
r = coderunner.Run(program_name, language, output, Input)

print("Status : " + r.getStatus())
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

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) file for the process of submitting pull requests to us.