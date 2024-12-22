from setuptools import setup, find_packages

setup(
    name='mhmixtools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',  # List your package dependencies here
    ],
    author='Md. Mahmud Hasan',
    description='A utility package for image generation and random data tasks',
    license='MIT',
)
