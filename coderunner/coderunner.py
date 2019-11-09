"""coderunner helps you run your programs on Judge0's Server"""
import requests

# language IDs on judge0, see README.md
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


class Run:
    """
    Initialize program data like name,expected input/output etc
    """

    def __init__(self, program_name: str, lang: str, output: str, inp: str = None):
        self.program_name = program_name
        self.lang = lang
        if lang not in languages:
            raise ValueError(f"{lang} is not a supported language {languages.keys()}")

        self.output = output
        self.inp = inp
        self.language_id = languages[lang]
        self.__response = None
        self.__memory = None
        self.__time = None
        self.__stdout = None

    def __readCode(self):
        """
        Read Source Code & return as string
        """
        with open(self.program_name, "r") as myfile:
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
            req = requests.get(API_URL + token["token"])
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
        api_params["source_code"] = self.program_name

        res = requests.post(API_URL, data=api_params)
        token = res.json()
        return token

    def getStandardOutput(self):
        """
        Return the standard output of the program
        """
        return self.__stdout

    def getMemory(self):
        """
        Return the memory used by the program (in bytes)
        """
        return self.__memory

    def getError(self):
        """
        Return any error occured during program execution
        """
        if self.__response["stderr"] != "":
            return self.__response["stderr"]
        return None

    def getTime(self):
        """
        Return execution time used by the program
        """
        return self.__time

    def getStatus(self):
        """
        Submits the program on Judge0's server and returns its status
        """
        self.program_name = self.__readCode()
        self.output = self.__readExpectedOutput()

        if self.inp is not None:
            self.inp = self.__readStandardInput()
            token = self.__submit()
            status = self.__readStatus(token)
        else:
            token = self.__submit()
            status = self.__readStatus(token)
        return status
