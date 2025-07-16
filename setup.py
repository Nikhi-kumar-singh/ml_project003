from setuptools import find_packages,setup
from typing import List
import warnings
warnings.filterwarnings("ignore")


def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    try:
        reqirement_file_path="requirements.txt"
        with  open(reqirement_file_path,"r") as file:
            lines=file.readlines()
            # print(lines)

        for line in lines:
            requirement=line.strip()
            if requirement and requirement != "-e .":
                 requirements_list.append(requirement)

    except Exception as e:
        print(e)

    return requirements_list




setup(
    name="Network Security",
    version="0.0.0",
    author="nikhil kumar",
    author_email="nikhilkumarsingh5872@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)





if __name__=="__main__":
    req=get_requirements()
    print(f"requirements : {req}")