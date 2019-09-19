import requests
import time
import sys

# language IDs on judge0, see README.md
languages = {
	"C++" : 10,
	"Java" : 27,
	"Python": 34,
	"C": 4
}

api_params = {
    "number_of_runs": "1",
    "cpu_time_limit": "2",
    "cpu_extra_time": "0.5",
    "wall_time_limit": "5",
    "memory_limit": "128000",
    "stack_limit": "64000",
    "max_processes_and_or_threads": "30",
    "enable_per_process_and_thread_time_limit": 'false',
    "enable_per_process_and_thread_memory_limit": 'true',
    "max_file_size": "1024"
}



def readCode(program):
	with open(program, 'r') as myfile:
		data = myfile.read()
	return data


def readExpectedOutput(output_file):
	with open(output_file, 'r') as out:
		data = out.read()
	return data


def readStandardInput(output_file):
	with open(output_file, 'r') as out:
		data = out.read()
	return data


def readStatus(token):
	while True:
		req = requests.get("https://api.judge0.com/submissions/" + token['token'])
		response = req.json()
		status = response['status']['description']
		if status != "Processing" and status != "In Queue":
			break
		print(status)

	if status == "Accepted":
		print(f'Output : \n{response["stdout"]}')
		print("Compile Success ✅")
		return status
	else:
		return response

def submit(program, language_id, *argv):
	if len(argv) == 2:
		stdout = argv[0]
		stdin = argv[1]
		api_params['stdin'] = stdin
	elif len(argv) == 1:
		stdout = argv[0]
	
	api_params['expected_output'] = stdout
	api_params['language_id'] = language_id
	api_params['source_code'] = program

	res = requests.post("https://api.judge0.com/submissions", data=api_params)
	token = res.json()
	return token


def run(program, language, *argv):
	program = readCode(program)
	stdout = readExpectedOutput(argv[0])
	
	if len(argv) == 2:
		stdin = readStandardInput(argv[1])
		token = submit(program, languages[language], stdout, stdin)
		status = readStatus(token)
	elif len(argv) == 1:
		token = submit(program, languages[language], stdout)
		status = readStatus(token)
	return status
