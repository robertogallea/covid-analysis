from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='covid_analysis',
      packages=find_packages(),
      version='0.0.5',
      description='Covid Analysys',
      author='Roberto Gallea',
      author_email='write@robertogallea.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)