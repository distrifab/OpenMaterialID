import logging
import json
import cbor2
from lark import Lark, Token, Tree

logging = logging.getLogger(__name__)

class BaseClass:

  internal = ['_BaseClass__renames']

  def __init__(self):
    self.__renames = self.__class__.__dict__.get('__renames', {})

  def __str__(self):
    return json.dumps(self.dump(), indent=2)

  def dump(self, rename=False):
    logging.debug(f"Dumping {self.__class__.__name__}")
    data = {}
    for key, value in self.__dict__.items():
      if key in self.internal:
        continue
      key_name = key
      if rename and key in self.__renames:
        key_name = self.__renames[key]
      if isinstance(value, BaseClass):
        data[key_name] = value.dump(rename=rename)
      else:
        data[key_name] = value
    return data

  def dump_cbor(self):
    logging.info(f"Dumping {self.__class__.__name__} to CBOR")
    data = self.dump(rename=True)
    bin = cbor2.dumps(data)
    logging.info(f"Dumped {len(bin)} bytes:")
    logging.info(bin)
    return bin

class Schema:

  def __init__(self, name, schema):
    import os
    filename = os.path.join(os.path.dirname(__file__), 'ipld.lark')
    with open(filename, 'r') as f:
      ipld_grammar = f.read()
      self.parser = Lark(
        ipld_grammar,
        start='start',
        parser='lalr',
      )
    self.tree = self.parser.parse(schema)
    self.root_instance = self.make_class(name, self.tree.children)()
    logging.info(f"Loaded {name} schema")
  
  def unpack_names(self, data, instance=None):
    unpacked = {}
    if instance == None:
      instance = getattr(self.root_instance, self.populate_id)
    renames = instance._BaseClass__renames
    if type(data) == dict:
      for key, value in data.items():
        expanded_key = key
        for long, short in renames.items():
          if short == key:
            expanded_key = long
        if type(value) == dict:
          child_instance = getattr(instance, expanded_key)
          value = self.unpack_names(value, child_instance)
        unpacked[expanded_key] = value
    return unpacked

  def find_type(self, tree, id):
    for child in tree.children:
      if child.data == 'struct_field':
        if child.children[0].children[0].value == id:
          # found node with id
          for child in child.children:
            if child.data == 'type':
              # found type
              id_type = child.children[0].children[0].value
              return id_type

  def walk(self, root_tree, tree, data, root_instance, instance):
    if type(data) == dict:
      for key, value in data.items():
        if type(value) == dict:
          type_id = self.find_type(tree, key)
          child_instance = getattr(root_instance, type_id)() # type:ignore
          new_tree = self.get_node(root_tree, type_id)
          self.walk(root_tree, new_tree, value, root_instance, child_instance)
          setattr(instance, key, child_instance)
        else:
          setattr(instance, key, value)
    else:
      logging.error(f"Unsupported data type: {str(type(data))}")

  def get_node(self, tree, id):
    for child in tree.children:
      if type(child) == Tree:
        if child.data == 'id' and child.children[0].value == id: # type:ignore
          return tree
        sub = self.get_node(child, id)
        if sub:
          return sub

  def load(self, populate_id, data):
    self.populate_id = populate_id
    instance = getattr(self.root_instance, populate_id)()
    node = self.get_node(self.tree, populate_id)
    self.walk(self.tree, node, data, self.root_instance, instance)
    setattr(self.root_instance, populate_id, instance)
    logging.info(f"Loaded {populate_id} data")
    return getattr(self.root_instance, populate_id)

  def make_type(self, typename):
    try:
      # TODO unsafe
      return eval(typename)
    except NameError:
      raise ValueError(f"Unsupported type: {typename}")

  def get_type_token(self, children, root_class):
    # get the type node from children properties
    for child in children:
      if child.data == 'type':

        # primitive type
        if len(child.children[0].children) == 0:
          return self.make_type(child.children[0].data)

        # typedef
        if isinstance(child.children[0].children[0], Token):
          child_type = child.children[0].children[0].value

          # typed kind
          if child_type in root_class:
            child_type = root_class[child_type]

          # TODO recursive type (eg Person with `relative: Person`)
          else:
            child_type = child.children[0].children[0].value

        # typed combined type (eg list, map)
        if isinstance(child.children[0].children[0], Tree):
          super_type = self.make_type(child.children[0].data)
          # TODO python does not support type enforcement
          # child_type = parent_type(self.get_type(child.children[0].children, parent))
          child_type = super_type

        return child_type

  def get_rename(self, children):
    for child in children:
      if child.data == 'repr_change':
        if child.children[0].children[0].value == 'rename':
          return child.children[1].children[0].children[0].value[1:-1]

  def make_class(self, name, children, root_class=None):
    class_object = {
      '__renames': {},
    }
    if root_class == None:
      root_class = class_object

    for child in children:

      if child.data == 'struct_declaration':
        # type_name = child.children.pop(0).children[0].value
        type_name = child.children[0].children[0].value
        type_class = self.make_class(type_name, child.children, root_class)
        class_object[type_name] = type_class

      elif child.data == 'typed_kind':
        type_name = child.children[0].children[0].value
        type_kind = child.children[1].children[0].data
        class_object[type_name] = self.make_type(type_kind)

      elif child.data == 'struct_field':
        field_name = child.children[0].children[0].value
        field_type = self.get_type_token(child.children, root_class)
        field_rename = self.get_rename(child.children)
        if field_rename:
          class_object['__renames'][field_name] = field_rename
        class_object[field_name] = field_type # type:ignore

      else:
        logging.debug(f"Unsupported data: {child.data}")
    
    logging.debug(f'Creating class {name} with {class_object}')
    class_template = type(name, (BaseClass,), class_object)
    logging.debug(f'Created class {class_template}')
    return class_template
