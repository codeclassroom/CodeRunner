"""
coderunner.py
====================================
The core module of CodeRunner
"""
import json
import os
import urllib.parse
import urllib.request

# language IDs on judge0, see Documentation
languages = {
    "Assembly": 45,
    "Bash": 46,
    "Basic": 47,
    "C": 50,
    "C++": 54,
    "C#": 51,
    "Common Lisp": 55,
    "D": 56,
    "Elixir": 57,
    "Erlang": 58,
    "Executable": 44,
    "Fortran": 59,
    "Go": 60,
    "Haskell": 61,
    "Java": 62,
    "JavaScript": 63,
    "Lua": 64,
    "OCaml": 65,
    "Octave": 66,
    "Pascal": 67,
    "PHP": 68,
    "Plain Text": 43,
    "Prolog": 69,
    "Python2": 70,
    "Python3": 71,
    "Ruby": 72,
    "Rust": 73,
    "TypeScript": 74,
}

api_params = {
    "cpu_time_limit": "2",
    "cpu_extra_time": "0.5",
    "wall_time_limit": "5",
    "memory_limit": "128000",
    "stack_limit": "64000",
    "max_processes_and_or_threads": "30",
    "enable_per_process_and_thread_time_limit": "false",
    "enable_per_process_and_thread_memory_limit": "false",
    "max_file_size": "1024",
}

API_URL = "https://api.judge0.com/submissions/"
FIELDS = "?fields=stdout,memory,time,status,stderr,exit_code,created_at"


class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""


class code:
    """
    Args:
        - Source Code
        - Language
        - Expected Output
        - Standard Input (Optional)
        - path (optional)
    """

    def __init__(
        self,
        source: str,
        lang: str,
        output: str = None,
        inp: str = None,
        path: bool = True,
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
        self.languages = list(languages.keys())

        if self.path:
            if not os.path.exists(source):
                raise OSError(f"{source} is not a valid file path")
            self.source = source

            if output is not None and not os.path.exists(output):
                raise OSError(f"{output} is not a valid file path")
            self.output = output

            if inp is not None and not os.path.exists(inp):
                raise OSError(f"{inp} is not a valid file path")
            self.inp = inp
        self.source = source
        self.output = output
        self.inp = inp

    def __readCode(self):
        try:
            with open(self.source, "r") as program_file:
                data = program_file.read()
            return data
        except FileNotFoundError as e:
            raise e

    def __readExpectedOutput(self):
        try:
            with open(self.output, "r") as exp_out:
                data = exp_out.read()
            return data
        except FileNotFoundError as e:
            raise e

    def __readStandardInput(self):
        try:
            with open(self.inp, "r") as standard_input:
                data = standard_input.read()
            return data
        except FileNotFoundError as e:
            raise e

    def __readStatus(self, token: str):
        """
        Check Submission status
        """
        while True:
            req = urllib.request.Request(API_URL + token["token"] + FIELDS)
            with urllib.request.urlopen(req) as response:
                req = response.read()

            self.__response = json.loads(req.decode("utf-8"))
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
        if self.output is not None:
            api_params["expected_output"] = self.output

        api_params["language_id"] = self.language_id
        api_params["source_code"] = self.source

        post_data = urllib.parse.urlencode(api_params).encode("ascii")
        req = urllib.request.Request(API_URL, post_data)
        with urllib.request.urlopen(req) as response:
            req = response.read()
        token = json.loads(req.decode("utf-8"))

        return token

    def getSubmissionDate(self):
        """Submission date/time of program"""
        return self.__response["created_at"]

    def getExitCode(self):
        """Exitcode of program (0 or 1)"""
        return self.__response["exit_code"]

    def getOutput(self):
        """Standard output of the program"""
        return self.__stdout

    def getMemory(self):
        """Memory used by the program"""
        return self.__memory

    def getError(self):
        """Error occured during execution of program"""
        if self.__response["stderr"] != "":
            return self.__response["stderr"]
        return None

    def getTime(self):
        """Execution time of program"""
        return self.__time

    def setFlags(self, options: str):
        """Options for the compiler (i.e. compiler flags)"""
        try:
            if len(options) > 128:
                raise ValueTooLargeError
            api_params["compiler_options"] = options
        except ValueTooLargeError:
            print("Maximum 128 characters allowed")

    def setArguments(self, arguments: str):
        """Command line arguments for the program"""
        try:
            if len(arguments) > 128:
                raise ValueTooLargeError
            api_params["command_line_arguments"] = arguments
        except ValueTooLargeError:
            print("Maximum 128 characters allowed")

    def run(self, number_of_runs: int = 1):
        """Submit the source code on judge0's server & return status"""
        api_params["number_of_runs"] = number_of_runs

        if os.path.exists(self.source):
            if self.path:
                if self.inp is not None:
                    self.inp = self.__readStandardInput()
                if self.output is not None:
                    self.output = self.__readExpectedOutput()
                self.source = self.__readCode()

        token = self.__submit()
        self.__token = token

    def getStatus(self):
        """Submission status"""
        status = self.__readStatus(self.__token)

        return status
