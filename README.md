# cc-judge
> The future judge for CodeClassroom.(_WIP_)


### Installation
1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git clone https://github.com/codeclassroom/cc-judge.git
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

Import the `run` method from *judge.py*.

```python
from judge import run

program_name = "test_python.py"
language = "Python"
output = "output.txt"

status = run(program_name, language, output)
print(status)
```


### Pointers ✏
- In a `Java` program the class name should always be ***`Main`***.


### TODO 📑
```
❌ Compile multiple files asynchronously.
✅ Convert the whole script into a module.
❌ Add --help to display script usage.
❌ Return live status of the submission.
```

### Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)
