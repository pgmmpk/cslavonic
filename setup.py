from setuptools import setup, find_packages
from os import path
from cslavonic import __version__, __description__, __keywords__, __url__, __author__, __author_email__


setup(
    name='cslavonic',
    version=__version__,
    description=__description__,
    keywords=__keywords__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,

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

    packages=find_packages(),

    install_requires=['fonttools'],

    package_data={'cslavonic': ['resources/untitlo.tsv']},

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'cu_codechart=cslavonic.cu_codechart:main',
            'cu_normalize=cslavonic.cu_normalize:main',
            'cu_reencode=cslavonic.cu_reencode:main',
        ],
    },
)
