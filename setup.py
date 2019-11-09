import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coderunner",
    version="0.3",
    author="Bhupesh Varshey",
    author_email="varsheybhupesh@gmail.com",
    description="Judge0 API Interface written in Python",
    keywords='judge0 coderunner judge0-api codeclassroom',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/CodeRunner",
    project_urls={
        "Documentation": "https://github.com/codeclassroom/CodeRunner/wiki/Documentation---coderunner-v0.3",
        "Source Code": "https://github.com/codeclassroom/CodeRunner",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/CodeRunner/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
    },
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