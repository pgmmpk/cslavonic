from setuptools import setup
from os import path
import codecs

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cslavonic',
    version='0.1.0',
    description='Utilities for working with Church Slavonic language',
    long_description=long_description,
    url='https://github.com/pgmmpk/cslavonic',

    author='Mike Kroutikov',
    author_email='pgmmpk@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
    ],

    keywords='church slavonic language',

    packages=['cslavonic'],

    install_requires=['fonttools'],

    entry_points={
        'console_scripts': [
            'codechart=cslavonic.codechart',
            'fix_uk=cslavonic.fix_uk',
            'ucs_to_utf8=cslavonic.ucs_to_utf8',
        ],
    },
)
