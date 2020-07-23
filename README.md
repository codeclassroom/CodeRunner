# CodeRunner 🏃

> A judge 👨🏽‍⚖️ for your programs, run and test your programs using Python


![PyPI](https://img.shields.io/pypi/v/coderunner?color=blue)
[![Build Status](https://travis-ci.org/codeclassroom/CodeRunner.svg?branch=master)](https://travis-ci.org/codeclassroom/CodeRunner)
[![codecov](https://codecov.io/gh/codeclassroom/CodeRunner/branch/master/graph/badge.svg)](https://codecov.io/gh/codeclassroom/CodeRunner)
![PyPI - Format](https://img.shields.io/pypi/format/coderunner?color=orange)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/coderunner)
[![Documentation Status](https://readthedocs.org/projects/coderunner/badge/?version=latest)](https://coderunner.readthedocs.io/en/latest/?badge=latest)
![PyPI - Downloads](https://img.shields.io/pypi/dm/coderunner?color=blue)


## Installation

Install using `pip` from PyPI

```bash
pip install coderunner
```

or directly from GitHub if you cannot wait to test new features

```bash
pip install git+https://github.com/codeclassroom/CodeRunner.git
```

## Usage

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

# run the code
r.run()

print("Running r :")
print("Status : " + r.getStatus())
print("Output : " + r.getOutput())

# See Documentation for more methods.
```

## Documentation

> [CodeRunner Documentation](https://coderunner.readthedocs.io/en/latest/)


## Development

##### Prerequisites
- Python 3.6+
- virtualenv

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
python tests.py
```
5. Lint the project with
```bash
flake8 coderunner --max-line-length=88 --ignore=F401
black --check --diff coderunner
```

## 📝 Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for details.

## :fire: Powered By
**[Judge0 API](https://github.com/judge0/api) - Free, robust and scalable open-source online code execution system**

## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.
