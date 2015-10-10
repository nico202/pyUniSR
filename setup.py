import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyUniSR",
    version = "0.0.2",
    author = "Nicolo Balzarotti",
    author_email = "anothersms@gmail.com",
    description = ("Python class to access studenti.unisr.it (Univerity Vita-Salute San Raffaele, Milano)"),
    license = "GPLv2",
    keywords = "unisr class milano university raffaele",
    url = "https://github.com/nico202/pyUniSR",
    packages=['UniSR'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv2 License",
    ],
)
