# flake8: noqa
from setuptools import setup

def load_requirements(path='requirements.txt'):
    with open(path) as f:
        return f.read().splitlines()[1:]

setup(name='worktag',
    version='0.0.1',
    description='A simple workspace tagging and retrieval tool',
    url='http://github.com/SeedyROM/worktag',
    author='Zack Kollar',
    author_email='me@seedyrom.io',
    license='MIT',
    packages=['worktag'],
    install_requires=load_requirements(),
    entry_points = {
        'console_scripts': ['wtag=worktag.__main__:main'],
    },
    zip_safe=False
)