from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stock-analyzer',
    version='0.1.0',
    description='A simple way to get stock indicators',
    long_description=readme,
    author='Thais Amorim',
    url='https://github.com/thasmarinho/stock-analyzer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
