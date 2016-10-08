import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='fulgore',
    version='0.0.1',
    install_requires=required,
    description='Communicates with Raspberry and MQTT',
    author='sergioaugrod',
    author_email='sergioaugrod@gmail.com',
    url='https://github.com/sergioaugrod/fulgore',
    packages=find_packages(exclude=('tests', 'docs'))
)
