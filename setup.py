from setuptools import setup, find_packages

setup(
    name='lib',
    version='0.0.0',
    description='lib library for docker-compose',
    author='Surya Rastogi',
    author_email='suryansh@gmail.com',
    url='https://github.com/suryarastogi/jupyter-python-docker-compose',
    packages=find_packages(include=["lib", "lib.*"]),
    test_suite="tests",
)