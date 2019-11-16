# CodeRunner 🏃

> [Judge0 API](https://api.judge0.com/) Interface written in Python

![PyPI](https://img.shields.io/pypi/v/coderunner?color=blue)
[![Build Status](https://travis-ci.org/codeclassroom/CodeRunner.svg?branch=master)](https://travis-ci.org/codeclassroom/CodeRunner)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/coderunner)
[![Documentation Status](https://readthedocs.org/projects/coderunner/badge/?version=latest)](https://coderunner.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/coderunner)](https://pepy.tech/project/coderunner)
[![GitHub license](https://img.shields.io/github/license/codeclassroom/CodeRunner)](https://github.com/codeclassroom/CodeRunner/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/codeclassroom/CodeRunner?color=blueviolet)](https://github.com/codeclassroom/CodeRunner/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](http://makeapullrequest.com)


## Usage

- Install `coderunner`.

`pip install coderunner`

## Documentation

> [CodeRunner Documentation](https://coderunner.readthedocs.io/en/latest/)


## Testing

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
pylint coderunner --disable=bad-continuation,invalid-name,too-many-instance-attributes
```


## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.
