#
# EEPROM simulation
# MiFare Classic 1K
# 16 sectors, 4 blocks per sector, 16 cells per block
#

import logging

logging = logging.getLogger(__name__)

class EEPROM:

  def __init__(self):
    self.sectors = 16
    self.blocks_per_sector = 4
    self.cells_per_block = 16
    self.usable_blocks = 3
    self.total_usable_length = self.sectors * self.usable_blocks * self.cells_per_block
    last = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x07, 0x80, 0x69, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

    # every block has the same instance
    # block = [self.usable_blocks * [self.cells_per_block * [0x00]] + [last]]
    # memory = self.sectors * block

    # every sector has the same instance
    # block = [0x00 for _ in range(self.cells_per_block)]
    # sector = [block[:] for _ in range(self.usable_blocks)] + [last[:]]
    # memory = [sector[:] for _ in range(self.sectors)]

    # ugly but works
    memory = []
    for _ in range(self.sectors):
      block = []
      for _ in range(self.usable_blocks):
        cell = []
        for _ in range(self.cells_per_block):
          cell.append(0x00)
        block.append(cell)
      block.append(last)
      memory.append(block)
    self.memory = memory

  def hexdump(self):
    for sector in range(self.sectors):
      print()
      print(f'{24*"="} Sector {sector:02X} {24*"="}')
      for block in range(self.blocks_per_sector):
        print(f'Block {block+sector*4:02X}:', end='')
        for cell in range(self.cells_per_block):
          print(f' {self.memory[sector][block][cell]:02X}', end='')
        print(' | ', end='')
        for cell in range(self.cells_per_block):
          if (self.memory[sector][block][cell] < 0x20) or (self.memory[sector][block][cell] > 0x7E):
            print('.', end='')
          else:
            print(chr(self.memory[sector][block][cell]), end='')
        print()

  def load(self, data):
    index = 0
    length = len(data)
    for sector in range(self.sectors):
      for block in range(self.usable_blocks):
        for cell in range(self.cells_per_block):
          if index < length:
            self.memory[sector][block][cell] = data[index]
            index += 1
          else:
            remaining = (index / self.total_usable_length) * 100
            logging.info(f'Loaded {index} bytes ({remaining:.2f}%)')
            logging.info(f'End of data: Sector {sector}, Block {block}, Cell {cell}')
            return
  
  def dump(self):
    data = []
    for sector in range(self.sectors):
      for block in range(self.usable_blocks):
        for cell in range(self.cells_per_block):
          data.append(self.memory[sector][block][cell])
    logging.info(f'Dumped {len(data)} bytes')
    return bytes(data)
