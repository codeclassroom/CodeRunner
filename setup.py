import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coderunner",
    version="0.4",
    author="Bhupesh Varshey",
    author_email="varsheybhupesh@gmail.com",
    description="Judge0 API Interface written in Python",
    keywords='judge0 coderunner judge0-api codeclassroom',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/CodeRunner",
    project_urls={
        "Documentation": "https://coderunner.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/codeclassroom/CodeRunner",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/CodeRunner/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Topic :: Education",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)