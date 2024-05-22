# OpenMaterialID

Open Standard for Manufacturing Materials identification

## Schema

The OpenMaterialID spec is defined in IPLD Schema format, in the `schema` directory.

## Demo

To try out the OpenMaterialID schema, go to the `sample` folder and run `python demo.py`.

## Example

The `sample/FF-PLA-A110.yml` yaml file is provided as a datasource to populate the OpenMaterialID Schema. 

The schema will convert the data to CBOR format to be stored on an RFID chip:

> \xa9av\x02bpd\xa8bmniFrancofilanwBlue PLA Filament A 110asgPLA-110bcnjBlue A 110bch\x1a\x00\x11>\xb1bmmx\x1afused_filament_fabricationac\x84drohsjue:10/2011ereachcfdaaa\xf6ac\xa3ad\x19\x06\xd6bdt\x14aw\x19\x03\xe8bmd\xa9abo2024-02-28-1450ap\x19\xff\xd3bmd\x1ae\xdd\xf1\xfbbmlk8FW4V83M+Q7aw\x19\x03\xebal\x19\x01Pat\x14ad\x18\xc8ao\x18Zbpp\xadbdnopolylactic_acidbac\x81x\x1cthermoplastic_polyurethane:3ap\x82vfood_contact_materialsnbiodegradationbds\x19\x04\xd8aa\x01bmd\nah\xa2ad\x18KasaAcmfr\x19\x02\xd0bgt\x19\x02?bmp\x19\x05nbwa\x05ar\x06btd\x19\t\xecbsp\xa4bdc\x184bdf\x18\xc8aw\x187bew\x18\xf6bps\xa4ae\x82\x18\xcd\x18\xe1ab\x82\x187\x18Aam\x82\x14\x18\x1eah\x82\x05\x14bst\xa3at\x82\x0f\x18(ah\x82\x05\x18Fal\x19\x01mau\xa6premaining_weight oseen_date_first nseen_date_last lmax_humidity omax_temperature pcomputed_density 

This complete representation of the schema will take 560 bytes on the chip, which represents 72.92% of the available space on a 1K Mifare Classic tag. It will be stored in memory this way:

```
======================== Sector 00 ========================
Block 00: A9 61 76 02 62 70 64 A8 62 6D 6E 69 46 72 61 6E | .av.bpd.bmniFran
Block 01: 63 6F 66 69 6C 61 6E 77 42 6C 75 65 20 50 4C 41 | cofilanwBlue PLA
Block 02: 20 46 69 6C 61 6D 65 6E 74 20 41 20 31 31 30 61 |  Filament A 110a
Block 03: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 01 ========================
Block 04: 73 67 50 4C 41 2D 31 31 30 62 63 6E 6A 42 6C 75 | sgPLA-110bcnjBlu
Block 05: 65 20 41 20 31 31 30 62 63 68 1A 00 11 3E B1 62 | e A 110bch...>.b
Block 06: 6D 6D 78 1A 66 75 73 65 64 5F 66 69 6C 61 6D 65 | mmx.fused_filame
Block 07: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 02 ========================
Block 08: 6E 74 5F 66 61 62 72 69 63 61 74 69 6F 6E 61 63 | nt_fabricationac
Block 09: 84 64 72 6F 68 73 6A 75 65 3A 31 30 2F 32 30 31 | .drohsjue:10/201
Block 0A: 31 65 72 65 61 63 68 63 66 64 61 61 61 F6 61 63 | 1ereachcfdaaa.ac
Block 0B: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 03 ========================
Block 0C: A3 61 64 19 06 D6 62 64 74 14 61 77 19 03 E8 62 | .ad...bdt.aw...b
Block 0D: 6D 64 A9 61 62 6F 32 30 32 34 2D 30 32 2D 32 38 | md.abo2024-02-28
Block 0E: 2D 31 34 35 30 61 70 19 FF D3 62 6D 64 1A 65 DD | -1450ap...bmd.e.
Block 0F: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 04 ========================
Block 10: F1 FB 62 6D 6C 6B 38 46 57 34 56 38 33 4D 2B 51 | ..bmlk8FW4V83M+Q
Block 11: 37 61 77 19 03 EB 61 6C 19 01 50 61 74 14 61 64 | 7aw...al..Pat.ad
Block 12: 18 C8 61 6F 18 5A 62 70 70 AD 62 64 6E 6F 70 6F | ..ao.Zbpp.bdnopo
Block 13: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 05 ========================
Block 14: 6C 79 6C 61 63 74 69 63 5F 61 63 69 64 62 61 63 | lylactic_acidbac
Block 15: 81 78 1C 74 68 65 72 6D 6F 70 6C 61 73 74 69 63 | .x.thermoplastic
Block 16: 5F 70 6F 6C 79 75 72 65 74 68 61 6E 65 3A 33 61 | _polyurethane:3a
Block 17: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 06 ========================
Block 18: 70 82 76 66 6F 6F 64 5F 63 6F 6E 74 61 63 74 5F | p.vfood_contact_
Block 19: 6D 61 74 65 72 69 61 6C 73 6E 62 69 6F 64 65 67 | materialsnbiodeg
Block 1A: 72 61 64 61 74 69 6F 6E 62 64 73 19 04 D8 61 61 | radationbds...aa
Block 1B: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 07 ========================
Block 1C: 01 62 6D 64 0A 61 68 A2 61 64 18 4B 61 73 61 41 | .bmd.ah.ad.KasaA
Block 1D: 63 6D 66 72 19 02 D0 62 67 74 19 02 3F 62 6D 70 | cmfr...bgt..?bmp
Block 1E: 19 05 6E 62 77 61 05 61 72 06 62 74 64 19 09 EC | ..nbwa.ar.btd...
Block 1F: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 08 ========================
Block 20: 62 73 70 A4 62 64 63 18 34 62 64 66 18 C8 61 77 | bsp.bdc.4bdf..aw
Block 21: 18 37 62 65 77 18 F6 62 70 73 A4 61 65 82 18 CD | .7bew..bps.ae...
Block 22: 18 E1 61 62 82 18 37 18 41 61 6D 82 14 18 1E 61 | ..ab..7.Aam....a
Block 23: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 09 ========================
Block 24: 68 82 05 14 62 73 74 A3 61 74 82 0F 18 28 61 68 | h...bst.at...(ah
Block 25: 82 05 18 46 61 6C 19 01 6D 61 75 A6 70 72 65 6D | ...Fal..mau.prem
Block 26: 61 69 6E 69 6E 67 5F 77 65 69 67 68 74 20 6F 73 | aining_weight os
Block 27: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0A ========================
Block 28: 65 65 6E 5F 64 61 74 65 5F 66 69 72 73 74 20 6E | een_date_first n
Block 29: 73 65 65 6E 5F 64 61 74 65 5F 6C 61 73 74 20 6C | seen_date_last l
Block 2A: 6D 61 78 5F 68 75 6D 69 64 69 74 79 20 6F 6D 61 | max_humidity oma
Block 2B: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0B ========================
Block 2C: 78 5F 74 65 6D 70 65 72 61 74 75 72 65 20 70 63 | x_temperature pc
Block 2D: 6F 6D 70 75 74 65 64 5F 64 65 6E 73 69 74 79 20 | omputed_density 
Block 2E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 2F: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0C ========================
Block 30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 31: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 32: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 33: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0D ========================
Block 34: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 35: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 36: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 37: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0E ========================
Block 38: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 39: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 3A: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 3B: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......

======================== Sector 0F ========================
Block 3C: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 3D: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 3E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
Block 3F: 00 00 00 00 00 00 FF 07 80 69 FF FF FF FF FF FF | .........i......
```

