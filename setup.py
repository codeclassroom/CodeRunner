import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coderunner",
    version="0.2",
    author="Bhupesh Varshey",
    author_email="varsheybhupesh@gmail.com",
    description="Judge0 API Interface written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/CodeRunner",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)