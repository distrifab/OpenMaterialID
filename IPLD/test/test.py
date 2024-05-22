# base class for factory
class BaseClass():
  def __init__(self):
    pass
  def __str__(self):
    return f'{self.__class__.__name__}_instance({self.__dict__})'


# definition of parent class
parent_class_dict = {}

type_class_dict = {}
type_class_dict['value_a'] = int
type_class_dict['value_b'] = str
type_class = type('TypeClass', (BaseClass,), type_class_dict)
parent_class_dict['my_type'] = type_class

child_class_dict = {}
child_class_dict['my_value'] = parent_class_dict['my_type']
child_class = type('ChildClass', (BaseClass,), child_class_dict)
parent_class_dict['my_child'] = child_class

parent_class = type('ParentClass', (BaseClass,), parent_class_dict)

print(parent_class)
print(parent_class.my_type)
print(parent_class.my_type.value_a)
print(parent_class.my_child)

my_parent_instance = parent_class()
my_child_instance = getattr(my_parent_instance, 'my_child')()
my_type_instance = getattr(my_parent_instance, 'my_type')()
setattr(my_type_instance, 'value_a', 10)
setattr(my_type_instance, 'value_b', 'hello')
setattr(my_child_instance, 'my_value', my_type_instance)
setattr(my_parent_instance, 'my_child', my_child_instance)

print(my_parent_instance)
print(my_parent_instance.my_child)
print(my_parent_instance.my_child.my_value)

# parent_instance
#   my_type
#     value_a: int
#     value_b: str
#   child_instance
#     my_value: my_type
