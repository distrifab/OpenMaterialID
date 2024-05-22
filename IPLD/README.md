# IPLD Schema support for python

This will be abstracted to a separate library in the future

IPLD provides a way to define schemas for standardizing data structures. This is useful for defining data structures that can be serialized and deserialized to and from multiple formats.

It also allows data validation, specification (optional, default value...) and upgrading the schema without breaking the existing data. Any data that is optional and non populated will be ignored during serialization, which removes any limitations in the standard's definition while still maintaining compatibility and space efficiency.

The currently implemented output format is CBOR with renaming support. This allows to output a very concise binary format that will leave some space even with a complete implementation of the proposed format.

It could be quite easy to dynamically create a memory map of the eeprom data for a microcontroller to read and write data in a very efficient way.
