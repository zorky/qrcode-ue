# docker build -t qrcode .
# docker-compose run --rm qrcode
import json
import sys
import zlib
import os
from datetime import datetime

import base45
import cbor2
from cbor2 import loads
from cose.messages import CoseMessage
from json import dumps
from pprint import pprint

def read_data(file):
    with open(file, "r") as myfile:
        data=myfile.read()
    return data

def convert_timestamp(s):
    try:
        return datetime.utcfromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return s

def get_dgc(cbor):
    data = loads(cbor)
    # replace meaningless unix timestamps with readable timestamps
    data[4] = convert_timestamp(data[4])
    data[6] = convert_timestamp(data[6])
    return data

def decode(data):
    decoded = base45.b45decode(data)
    # decompress using zlib
    decompressed = zlib.decompress(decoded)
    # decode COSE message (no signature verification done)
    cose = CoseMessage.decode(decompressed)
    return cose

QRCODE = read_data("qr-code.txt")
if QRCODE[0:4] != 'HC1:':
    print('Pas un QR CODE valide')
    sys.exit(1)

print(f"CODE : {QRCODE[4:]}")
if QRCODE:
    cose = decode(QRCODE[4:])
    cbortag = loads(cose.payload)
    # print(cbortag)
    # dgc = {
    #     # 'tag': cbortag.tag,
    #     'alg': loads(cbortag.value[0]),
    #     'kid': get_kid(cbortag.value[1]),
    #     'dgc': get_dgc(cbortag.value[2]),
    #     'signature': cbortag.value[3].hex(),
    # }
    print(dumps(cbortag, indent=3))
