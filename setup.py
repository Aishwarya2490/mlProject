from setuptools import find_packages,setup
from typing import List


hyphen_e_dot = "-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    Return a list required libraries to be downloaded for project
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements
setup(
name = 'mlproject',
version = '0.0.1',
author = "Aishwarya",
author_email = 'aishwaryasrivastava27@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')  
# to load all required libraries like (there maybe 100 of libraries in a project so for easiness get_requirement function is used) - ['pandas','numpy','matplotlib','seaborn']
)