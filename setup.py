import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coderunner",
    version="0.8",
    license="MIT",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="A judge for your programs, run and test your programs through Python",
    keywords='judge0 coderunner judge0api codeclassroom ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeclassroom.github.io/CodeRunner/",
    project_urls={
        "Documentation": "https://coderunner.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/codeclassroom/CodeRunner",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/CodeRunner/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
        'Tracker': "https://github.com/codeclassroom/CodeRunner/issues",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Education",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
