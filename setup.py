"""
The setup.py file is crucial for any project, as it is an essential
part of packaging and distributing Python projects. 
It is used by Setuptools to define the configuration of a project,
such as its metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    :return: Description
    :rtype: List[str]
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list


setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Vivek Sharma",
    author_email="vivekshar2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)


