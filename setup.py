from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)-> List[str]:
    # this func will return requirements in the form of list
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Puneet',
    author_email= 'sharmapuneet8126@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)