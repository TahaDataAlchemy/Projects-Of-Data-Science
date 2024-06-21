# #Primary purpose ye hai is file ko banane ka k hum apna project as a package istamal karsakte like library ki tarha import or download karsakte hai 
from setuptools import find_packages, setup
from typing import List  # purpose : it is used that it will combine all packages that used in a program and the main thing that is some one download it he/she will never have to worry about the packages of all code present in a project because find_my_packages will combien all and it is easy to downloda

HYPHEN_E_DOT = '-e .'    # (Also Called Editable Mode) use because setup will run multiple times so it will not start downloading again & again requirments and if any change happen it will reflect to it immediately


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from the specified file path.
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and not req.strip().startswith("#")]

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    
    return requirements



setup(
    name="END TO END MLOPS PROJECT",
    version="0.01",
    author="Taha",
    author_email="tahamehboob281@gmail.com",
    packages=find_packages(),  # it will see in all folder of project if __init__.py file there it will fetch those files and build them, build them so they can be import like sseaborn
    install_requires=get_requirements("requirements.txt"),  # Fetching requirements from requirements.txt
)
