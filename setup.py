from setuptools import setup, find_packages

setup(
    name='mhmixtools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 
        'bs4'
    ],
    author='Md. Mahmud Hasan',
    description='A utility package for image generation and random data tasks',
    license='MIT',
)
