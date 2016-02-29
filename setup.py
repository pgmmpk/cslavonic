from setuptools import setup
from os import path
import codecs

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cslavonic',
    version='0.2.0',
    
    description='Utilities for working with Church Slavonic language',
    long_description=long_description,
    
    url='https://github.com/pgmmpk/cslavonic',
    author='Mike Kroutikov',
    author_email='pgmmpk@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Religion',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    keywords='church slavonic language',

    packages=['cslavonic'],

    install_requires=['fonttools'],

    entry_points={
        'console_scripts': [
            'cu_codechart=cslavonic.codechart',
            'cu_normalize=cslavonic.fix_uk',
            'cu_reencode=cslavonic.ucs_to_utf8',
        ],
    },
)
