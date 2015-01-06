from setuptools import setup, find_packages

from forecaster import VERSION


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
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
