from setuptools import find_packages, setup
from typing import List




setup(
name='mlproject',
version='0.0.1',
author='Ekendra',
author_email='ekendra.9121988@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)