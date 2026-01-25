from setuptools import setup, find_packages

setup(
    name="HackerOneCsvGrabber",
    version="2.0.0",
    author="Victor Silva",
    description="A tool to extract and process in scope assets from Hacker One CSV files",
    packages=find_packages(include=["src", "src.*"]),
    package_dir={"": "."},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "HackerOneCsvGrabber=src.main:main",
        ],
    },
)