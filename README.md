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
4. Run this command to test the script.
```bash
python3 judge.py test_java.java Java output.txt
```

### Usage
Currently it can be used as a script only.

```bash
python3 judge.py *arg1* *arg2* *arg3* *arg4*  
```

1. `arg1` = Program to compile/interpret (e.g helloword.java, test.cpp).

2. `arg2` = programming language, currently available languages :
	- C++ (g++ 7.2.0)
	- Python (3.6.0)
	- Java (OpenJDK 8)
	- C (gcc 6.4.0)

3. `arg3` = Expected Output textfile (e.g output.txt)

4. `arg4` = Standard Input, a textfile which contains the input to program (e.g input.txt)

The whole command should look like.
```bash
python3 judge.py myfile.java Java output.txt input.txt
```
or if you don't have a `stdin`.
```bash
python3 judge.py myfile.java Java output.txt
```


### Pointers
- In a `Java` program the class name should always be ***Main***.


### TODO 📑
```
❌ Compile multiple files asynchronously.
❌ Convert the whole script into a module.
❌ Add --help to display script usage.
```

### Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)
