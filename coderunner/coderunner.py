"""
coderunner.py
====================================
The core module of CodeRunner
"""
import os

import requests

# language IDs on judge0, see Documentation
languages = {"C++": 10, "Java": 27, "Python": 34, "C": 4}

api_params = {
    "number_of_runs": "1",
    "cpu_time_limit": "2",
    "cpu_extra_time": "0.5",
    "wall_time_limit": "5",
    "memory_limit": "128000",
    "stack_limit": "64000",
    "max_processes_and_or_threads": "30",
    "enable_per_process_and_thread_time_limit": "false",
    "enable_per_process_and_thread_memory_limit": "true",
    "max_file_size": "1024",
}

API_URL = "https://api.judge0.com/submissions/"
FIELDS = "?fields=stdout,memory,time,status,stderr,exit_code,created_at"


class Run:
    """
    Args:
        - Source Code
        - Language
        - Expected Output
        - Standard Input (Optional)
        - path (optional)
    """

    def __init__(
        self, source: str, lang: str, output: str, inp: str = None, path: bool = True
    ):

        self.path = path
        if lang not in languages:
            raise ValueError(f"{lang} is not a supported language {languages.keys()}")
        self.lang = lang
        self.language_id = languages[lang]
        self.__response = None
        self.__memory = None
        self.__time = None
        self.__stdout = None

        if self.path:
            if not os.path.exists(source):
                raise OSError(f"{source} is not a valid file path")
            self.source = source

            if not os.path.exists(output):
                raise OSError(f"{output} is not a valid file path")
            self.output = output

            if inp is not None and not os.path.exists(inp):
                raise OSError(f"{inp} is not a valid file path")
            self.inp = inp
        self.source = source
        self.output = output
        self.inp = inp

    def __readCode(self):
        with open(self.source, "r") as myfile:
            data = myfile.read()
        return data

    def __readExpectedOutput(self):
        with open(self.output, "r") as out:
            data = out.read()
        return data

    def __readStandardInput(self):
        with open(self.inp, "r") as out:
            data = out.read()
        return data

    def __readStatus(self, token: str):
        """
        Check Submission status
        """
        while True:
            req = requests.get(API_URL + token["token"] + FIELDS)
            self.__response = req.json()
            self.__memory = self.__response["memory"]
            self.__time = self.__response["time"]
            status = self.__response["status"]["description"]
            if status not in ("Processing", "In Queue"):
                break

        if status == "Accepted":
            self.__stdout = self.__response["stdout"]
            return status
        return self.__response["status"]["description"]

    def __submit(self):
        if self.inp is not None:
            api_params["stdin"] = self.inp

        api_params["expected_output"] = self.output
        api_params["language_id"] = self.language_id
        api_params["source_code"] = self.source

        res = requests.post(API_URL, data=api_params)
        token = res.json()
        return token

    def getSubmissionDate(self):
        """
        return submission date/time of program
        """
        return self.__response["created_at"]

    def getExitCode(self):
        """
        return exitcode of program (0 or 1)
        """
        return self.__response["exit_code"]

    def getOutput(self):
        """
        return standard output of program
        """
        return self.__stdout

    def getMemory(self):
        """
        return memory used by the program
        """
        return self.__memory

    def getError(self):
        """
        return any error message occured during execution of program
        """
        if self.__response["stderr"] != "":
            return self.__response["stderr"]
        return None

    def getTime(self):
        """
        return execution time of program
        """
        return self.__time

    def getStatus(self):
        """
        submit the source code on judge0's server & return status
        """
        if self.path:
            if self.inp is not None:
                self.inp = self.__readStandardInput()
            self.source = self.__readCode()
            self.output = self.__readExpectedOutput()

        token = self.__submit()
        status = self.__readStatus(token)

        return status
