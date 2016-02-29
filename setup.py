from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))

setup(
    name='cslavonic',
    version='0.3.0',
    
    description='Utilities for working with Church Slavonic language',
    
    url='https://github.com/pgmmpk/cslavonic',
    download_url='https://github.com/pgmmpk/cslavonic/tarball/0.3.0',
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
            'cu_codechart=cslavonic.cu_codechart:main',
            'cu_normalize=cslavonic.cu_normalize:main',
            'cu_reencode=cslavonic.cu_reencode:main',
        ],
    },
)
