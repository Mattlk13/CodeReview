####################################################################################################
# 
# DiffViewer - Diff Viewer 
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

""" This module provides an implementation for enumerate.

The enum factory :func:`EnumFactory` builds a enumerate from a list of names and assigns to these
constants a value from 0 to ``N-1``, where ``N`` is the number of constants::

  enum1 = EnumFactory('Enum1', ('cst1', 'cst2'))
   
then we can get a constant's value using an integer context like::
     
  int(enum1.cst1)

and the constant's name using::

  repr(enum1.cst2)

The number of constants could be retrieved with::

  len(enum1)

The enum factory :func:`ExplicitEnumFactory` permits to specify the values of the constants::
        
  enum2 = ExplicitEnumFactory('Enum2', {'cst1':1, 'cst2':3})

We can test if a value is in the enum using::

  constant_value in enum2

"""

####################################################################################################

# __all__ = ['EnumFactory', 'ExplicitEnumFactory']

####################################################################################################

class ReadOnlyMetaClass(type):

    """ This meta class implements a class where the attributes are read only. """

    ###############################################

    def __setattr__(self, name, value):

        raise NotImplementedError

####################################################################################################

class EnumMetaClass(ReadOnlyMetaClass):

    """ This meta class implements the function :func:`len`. """

    ###############################################

    def __len__(self):

        return self._size

####################################################################################################

class ExplicitEnumMetaClass(ReadOnlyMetaClass):

    """ This meta class implements the operator ``in``. """

    ###############################################

    def __contains__(self, item):

        return item in self.constants

####################################################################################################

class EnumConstant(object):

    """ Define an Enum Constant """

    ##############################################
    
    def __init__(self, name, value):

        self._name = name
        self._value = value

    ##############################################
    
    def __eq__(self, other):

        return self._value == int(other)
        
    ##############################################
    
    def __int__(self):

        return self._value

    ##############################################
    
    def __repr__(self):

        return self._name
    
####################################################################################################

def EnumFactory(enum_name, enum_tuple):

    """ Return an :class:`EnumMetaClass` instance, where *enum_name* is the class name and
    *constant_names* is an iterable of constant's names.
    """

    obj_dict = {}
    obj_dict['_size'] = len(enum_tuple)
    for value, name in enumerate(enum_tuple):
        obj_dict[name] = EnumConstant(name, value)

    return EnumMetaClass(enum_name, (), obj_dict)

####################################################################################################

def ExplicitEnumFactory(enum_name, enum_dict):

    """ Return an :class:`ExplicitEnumMetaClass` instance, where *enum_name* is the class name and
    *constant_dict* is a dict of constant's names and their values.
    """

    obj_dict = {}
    obj_dict['constants'] = enum_dict.values()
    for name, value in enum_dict.items():
        obj_dict[name] = EnumConstant(name, value)

    return ExplicitEnumMetaClass(enum_name, (), obj_dict)

####################################################################################################
#
# End
#
####################################################################################################