import time
import sys
import requests

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

API_URL = "https://api.judge0.com/submissions/"

class coderunner:

	def __init__(self, program_name, lang, output, inp = None):
		self.program_name = program_name
		self.lang = lang
		self.output = output
		self.inp = inp
		self.language_id = languages[lang]

	def readCode(self):
		"""
		Read Source Code & return as string
		"""
		with open(self.program_name, 'r') as myfile:
			data = myfile.read()
		return data


	def readExpectedOutput(self):
		with open(self.output, 'r') as out:
			data = out.read()
		return data


	def readStandardInput(self):
		with open(self.inp, 'r') as out:
			data = out.read()
		return data


	def readStatus(self, token):
		"""
		Check Submission status
		"""
		while True:
			req = requests.get(API_URL + token['token'])
			response = req.json()
			status = response['status']['description']
			if status != "Processing" and status != "In Queue":
				break
			print(status)

		if status == "Accepted":
			#print(f'Output : \n{response["stdout"]}')
			print(f'Time : {response["time"]}')
			print("Compile Success ✅")
			return status
		else:
			return response['status']['description']

	def submit(self):
		if self.inp != None:
			api_params['stdin'] = self.inp
		
		api_params['expected_output'] = self.output
		api_params['language_id'] = self.language_id
		api_params['source_code'] = self.program_name

		res = requests.post(API_URL, data=api_params)
		token = res.json()
		return token


	def run(self):
		self.program_name = self.readCode()
		self.output = self.readExpectedOutput()
		
		if self.inp != None:
			self.inp = self.readStandardInput()
			token = self.submit()
			status = self.readStatus(token)
		else:
			token = self.submit()
			status = self.readStatus(token)
		return status

