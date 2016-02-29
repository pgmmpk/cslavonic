#coding: utf-8
'''
Machinery needed to register 'UCS' encoding as a valid python encoding.

To use UCS encoding, `ucs_codec.register_UCS()`

Created on Feb 4, 2016

@author: mike
'''
from __future__ import print_function, unicode_literals
import codecs
from cslavonic.ucs_decode import ucs_encode, ucs_decode

### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input_, errors='strict'):
        return ucs_encode(input_, errors)
    
    def decode(self, input_, errors='strict'):
        return ucs_decode(input_, errors)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input_, final=False):
        return ucs_encode(input_, self.errors)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input_, final=False):
        return ucs_decode(input_, self.errors)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

_ucs_codec_info = codecs.CodecInfo(
        name='UCS',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

def register_UCS():
    def search(encoding):
        if encoding in ('UCS', 'ucs'):
            return _ucs_codec_info
    codecs.register(search)
