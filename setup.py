from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'

def requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name='Ml_project',
    version='0.0.1',
    author='Sunny',
    author_email='sa2181780@gmail.com',
    packages=find_packages(),
    install_requires=requirements('requirements.txt')
)