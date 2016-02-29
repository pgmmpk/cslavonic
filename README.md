# cslavonic
[![Build Status](https://travis-ci.org/pgmmpk/cslavonic.svg?branch=master)](https://travis-ci.org/pgmmpk/cslavonic)

Utilities to work with [Church Slavonic language](https://en.wikipedia.org/wiki/Church_Slavonic_language)

* ucs_to_utf8 re-encodes text from legacy UCS encoding to Unicode utf-8
* codechart generates TeX document that tests fonts by showing characters in Unicode blocks used by Church Slavonic
* fix_uk Allows one to re-encode Church slavonic unicode text between two flavors of "uk" representation

# ucs_to_utf8
Many Church Slavonic texts are available in legacy encodings. Most prominent are:

* [USC encoding](http://www.irmologion.ru/ucsenc.html)
* [HIP encoding](http://www.orthlib.ru/hip/manual.html)

Since there are already tools to convert from HIP to UCS [see here](http://www.orthlib.ru/hip/manual.html), we
only need to cover UCS-to-Unicode leg.

This code is inspired by [Perl converter by Alexander Andreev](https://github.com/typiconman/Perl-Lingua-CU), and
uses its for the critical part - encoding tables. You can consider this to be a Python3 port of Alexander's work.

# codechart
Generates a XeLaTex document to test font, Use this to evaluate fonts that claim support for Church Slavonic.

This is a Python3 port of [original code by Alexander Andreev](https://github.com/typiconman/fonts-cu). The only 
rationale for this port is me not willing to install Perl :)

# fix_uk
Re-encodes between current (but retireing) handling of lowercase "uk" digraph in Unicode and upcoming (not yet 
approved as of Jan 2016) Unicode recommendation.

