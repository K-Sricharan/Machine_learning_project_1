from setuptools import setup
from typing import List 


 #declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
version = "0.0.3"
Author = "charan"
Requirement_file_name = "Requirement.txt"


def get_Requirement_list()->List[str]:
    """
     Description: This function is going to return list of requirement mention in requirements.txt file

     return this function is going to a list which will contain name of libraries mentioned in requirementtt file

    """
    with open(Requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
  name = PROJECT_NAME,
  version = version,
  author = Author,
  description = "This is the First FSDS Project",
  packages = ["housing"],
  install_requires = get_Requirement_list()
)

