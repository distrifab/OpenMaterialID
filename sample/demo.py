#
# This is a sample script to demonstrate
# the usage of OpenMaterialID schema and a MiFare Classic 1K EEPROM
#

import yaml
import cbor2
import logging

import sys
sys.path.append('..')
import IPLD
from eeprom import EEPROM

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

# name of the schema file and root class
schema_name = 'OpenMaterialID'

# name of the root instance object
root_id = 'MaterialID'

# datasource
filename = 'FF-PLA-A110.yml'

with open(f'../schema/{schema_name}.ipldsch', 'r') as f:
  schema = IPLD.Schema(schema_name, f.read())

with open(filename) as f:
  data_obj = yaml.load(f, Loader=yaml.FullLoader)
  data = schema.load(root_id, data_obj)

# write to EEPROM
eeprom = EEPROM()
bin = data.dump_cbor()
eeprom.load(bin)

# print written data
eeprom.hexdump()

# read from EEPROM
contents = eeprom.dump()
loaded = cbor2.loads(contents)
unpacked = schema.unpack_names(loaded)

# print read data
logging.info(f'{unpacked}')
