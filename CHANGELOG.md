# Changelog

All notable changes to this project will be documented in this file.

## [1.0] - June , 2020
⚠ **Major Update (Breaking Changes)**

### Added
- Add API key authorizations
- Custom API URL support

### Changed
- Due to Judge0 API going [freemium](https://github.com/judge0/api/issues/171), the default API URL, [https://api.judge0.com] is no longer available. To use the API signup for a plan on [RapidAPI](https://rapidapi.com/hermanzdosilovic/api/judge0/pricing) & use the token to access the API through coderunner.


## [0.8] - May 27, 2020

### Fix
- Fixed bug where compiling a Java program resulted in Compilation Error.


## [0.7] - Jan 19, 2020

### Changed
- `code()` class now ignores `output`. i.e you can just provide source code & language to run a program.


## [0.6] - Jan 5, 2020

### Added

- New optional argument, `number_of_runs`  in `run()` method, use this to specify no.of times you want to run the code. Default is set to 1.
- Ported NEW Languages. CodeRunner now supports all languages provided by Judge0.
- `setFlags(options)` for setting options for the compiler (i.e. compiler flags).
- `setArguments(arguments)` for setting Command line arguments for the program.

### Changed
- Minor internal improvemets.


## [0.5] - Dec 20, 2019

### Added

- New instance method - `run()`.
- `run()` is now used to run the code i.e the code is submitted to Judge0 api using this method.
- Support for *Bash 4.4*.

### Changed
- Renamed Class `Run` to `code` for easier usage.
- `getStatus()`, now only returns the status in comparison to earlier versions where it performed multiple tasks.
This is effect fixes [#2](https://github.com/codeclassroom/CodeRunner/issues/2).

### Removed
 - `requests` as a dependency, Network requests are now 50% faster.


## [0.4] - Nov 11, 2019

### Added

- `getSubmissionDate()`, `getExitCode` new methods.
- Official Documentation.

### Changed

- Class Run `init` - Now you can pass _source code_, _input_ and _output_ to program as strings (limited to file paths in prior versions).


## [0.3] - Nov 9, 2019

### Added

- Removed redundant imports
- Added Module/Class docstrings for documentation
- Formatted Code


## [0.2] - Oct 31, 2019

### Changed

- Fix import requests problem.


## [0.1] - Oct 30, 2019
- Initial Release