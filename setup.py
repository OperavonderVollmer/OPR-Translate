from setuptools import setup, find_packages

setup(
    name="OPR-Translate",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "deep_translator",
        "OperaPowerRelay @ git+https://github.com/OperavonderVollmer/OperaPowerRelay@main"
    ],
    python_requires=">=3.7",
    author="Opera von der Vollmer",
    description="Abstract Translator for consistency, used and made compatible for Opera's pipelines",
    url="https://github.com/OperavonderVollmer/OPR-Translate", 
    license="MIT",
)
