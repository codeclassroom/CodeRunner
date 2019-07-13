import requests
import time
import sys

# language IDs on judge0
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


def read_stdin(output_file):
	with open(output_file, 'r') as out:
		data = out.read()
	return data


def readStatus(token):
	while True:
		res = requests.get("https://api.judge0.com/submissions/" + token['token'])
		response = res.json()
		status = response['status']['description']
		#time.sleep(0.5) # wait for judge0 to compile
		if status != "Processing" and status != "In Queue":
			break

	print("Processing 🔵 , \n" + program)
	print("Expected Output : \n" + stdout)

	if response['status']['description'] == "Accepted":
		print("Output : \n" + str(response['stdout']))
		print("Compile Success ✅")
	else:
		print("Compile Failed ❌")
		print("Output : " + str(response['stdout']))
		print("Error : " + str(response['stderr']))
		print("Message : " + str(response['message']) + ", " + response['status']['description'])


def compile(program, language_id, *argv):
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
	readStatus(token)


if __name__ == '__main__':
	if len(sys.argv) == 4:
		program = sys.argv[1]
		language = sys.argv[2]
		output_file = sys.argv[3]
		stdout = readExpectedOutput(output_file)
		inputCode = readCode(program)
		compile(inputCode, languages[language],stdout)

	elif len(sys.argv) == 5:
		program = sys.argv[1]
		language = sys.argv[2]
		output_file = sys.argv[3]
		in_file = sys.argv[4]
		stdin = read_stdin(in_file)
		stdout = readExpectedOutput(output_file)
		inputCode = readCode(program)
		compile(inputCode, languages[language], stdout, stdin)