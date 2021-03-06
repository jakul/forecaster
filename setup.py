from setuptools import setup, find_packages
import sys
import os

from forecaster import VERSION


if sys.argv[-1] == 'tag-version':
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

setup(
    name='forecaster',
    version=VERSION,
    description=(
        'Forecaster lets you find out what the weather will be where you are '
        'using the openweathermap.org REST API'
    ),
    author='Craig Blaszczyk',
    author_email='masterjakul@gmail.com',
    url='https://github.com/jakul/forecaster',
    license='BSD',
    packages=find_packages(),
    package_data = {
        '': ['version.txt',]
    },
    #TODO: auto read this from requirements.txt
    install_requires=['requests',],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
