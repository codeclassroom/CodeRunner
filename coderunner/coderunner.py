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

class Run:

	def __init__(self, program_name: str, lang: str, output: str, inp: str = None):
		self.program_name = program_name
		self.lang = lang
		if lang not in languages:
			raise ValueError(f"{lang} is not a supported languige {languages.keys()}")
		
		self.output = output
		self.inp = inp
		self.language_id = languages[lang]

	def __readCode(self):
		"""
		Read Source Code & return as string
		"""
		with open(self.program_name, 'r') as myfile:
			data = myfile.read()
		return data


	def __readExpectedOutput(self):
		with open(self.output, 'r') as out:
			data = out.read()
		return data


	def __readStandardInput(self):
		with open(self.inp, 'r') as out:
			data = out.read()
		return data


	def __readStatus(self, token: str):
		"""
		Check Submission status
		"""
		while True:
			req = requests.get(API_URL + token['token'])
			self.__response = req.json()
			self.__memory = self.__response["memory"]
			self.__time = self.__response["time"]
			status = self.__response['status']['description']
			if status != "Processing" and status != "In Queue":
				break

		if status == "Accepted":
			self.__stdout = self.__response["stdout"]
			return status
		else:
			return self.__response['status']['description']

	def __submit(self):
		if self.inp != None:
			api_params['stdin'] = self.inp
		
		api_params['expected_output'] = self.output
		api_params['language_id'] = self.language_id
		api_params['source_code'] = self.program_name

		res = requests.post(API_URL, data=api_params)
		token = res.json()
		return token


	def getStandardOutput(self):
		return self.__stdout


	def getMemory(self):
		return self.__memory


	def getError(self):
		if self.__response['stderr'] != '':
			return self.__response['stderr']
		return None


	def getTime(self):
		return self.__time


	def getStatus(self):
		self.program_name = self.__readCode()
		self.output = self.__readExpectedOutput()
		
		if self.inp != None:
			self.inp = self.__readStandardInput()
			token = self.__submit()
			status = self.__readStatus(token)
		else:
			token = self.__submit()
			status = self.__readStatus(token)
		return status

