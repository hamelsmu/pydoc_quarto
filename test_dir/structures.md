
# requests.structures

## Description
    

## Classes
    builtins.dict(builtins.object)
        LookupDict
    collections.abc.MutableMapping(collections.abc.Mapping)
        CaseInsensitiveDict
    

### CaseInsensitiveDict

<strong>class CaseInsensitiveDict(collections.abc.MutableMapping)</strong>

     |  CaseInsensitiveDict(data=None, **kwargs)
     |  
     |  A case-insensitive ``dict``-like object.
     |  
     |  Implements all methods and operations of
     |  ``MutableMapping`` as well as dict's ``copy``. Also
     |  provides ``lower_items``.
     |  
     |  All keys are expected to be strings. The structure remembers the
     |  case of the last key to be set, and ``iter(instance)``,
     |  ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
     |  will contain case-sensitive keys. However, querying and contains
     |  testing is case insensitive::
     |  
     |      cid = CaseInsensitiveDict()
     |      cid['Accept'] = 'application/json'
     |      cid['aCCEPT'] == 'application/json'  # True
     |      list(cid) == ['Accept']  # True
     |  
     |  For example, ``headers['content-encoding']`` will return the
     |  value of a ``'Content-Encoding'`` response header, regardless
     |  of how the header name was originally stored.
     |  
     |  If the constructor, ``.update``, or equality comparison
     |  operations are given keys that have equal ``.lower()``s, the
     |  behavior is undefined.
     |  
     |  Method resolution order:
     |      CaseInsensitiveDict
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __delitem__(self, key)
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __getitem__(self, key)
     |  
     |  __init__(self, data=None, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __len__(self)
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __setitem__(self, key, value)
     |  
     |  copy(self)
     |      # Copy is required
     |  
     |  lower_items(self)
     |      Like iteritems(), but with all lowercase keys.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  __hash__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |  
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  pop(self, key, default=<object object at 0x10077c180>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |  
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |  
     |  __contains__(self, key)
     |  
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |  
     |  __reversed__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |  
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |      
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |  
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |      
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
    

### LookupDict

<strong>class LookupDict(builtins.dict)</strong>

     |  LookupDict(name=None)
     |  
     |  Dictionary lookup object.
     |  
     |  Method resolution order:
     |      LookupDict
     |      builtins.dict
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getitem__(self, key)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __init__(self, name=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  get(self, key, default=None)
     |      Return the value for key if key is in the dictionary, else default.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.dict:
     |  
     |  __contains__(self, key, /)
     |      True if the dictionary has the specified key, else False.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __ior__(self, value, /)
     |      Return self|=value.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the dict keys.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(...)
     |      D.__sizeof__() -> size of D in memory, in bytes
     |  
     |  clear(...)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |  
     |  items(...)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(...)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  pop(...)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      
     |      If the key is not found, return the default if given; otherwise,
     |      raise a KeyError.
     |  
     |  popitem(self, /)
     |      Remove and return a (key, value) pair as a 2-tuple.
     |      
     |      Pairs are returned in LIFO (last-in, first-out) order.
     |      Raises KeyError if the dict is empty.
     |  
     |  setdefault(self, key, default=None, /)
     |      Insert key with a value of default if key is not in the dictionary.
     |      
     |      Return the value for key if key is in the dictionary, else default.
     |  
     |  update(...)
     |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
     |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
     |      In either case, this is followed by: for k in F:  D[k] = F[k]
     |  
     |  values(...)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.dict:
     |  
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585
     |  
     |  fromkeys(iterable, value=None, /) from builtins.type
     |      Create a new dictionary with keys from iterable and values set to value.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.dict:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from builtins.dict:
     |  
     |  __hash__ = None