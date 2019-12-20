# Changelog

All notable changes to this project will be documented in this file.


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