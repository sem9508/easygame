from setuptools import setup, find_packages

setup(
    name='EasyGame',
    version='0.1',
    packages=find_packages(),
    description='A framework for game development tools and components.',
    author='hahaeasy',
    install_requires=[
        'pygame>=2.0.0'
    ],
)
