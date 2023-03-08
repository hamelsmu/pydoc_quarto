
# requests.cookies

## Description
    
    

## Classes
    builtins.RuntimeError(builtins.Exception)
        CookieConflictError
    builtins.object
        MockRequest
        MockResponse
    collections.abc.MutableMapping(collections.abc.Mapping)
        RequestsCookieJar(http.cookiejar.CookieJar, collections.abc.MutableMapping)
    http.cookiejar.CookieJar(builtins.object)
        RequestsCookieJar(http.cookiejar.CookieJar, collections.abc.MutableMapping)
    

### CookieConflictError

<strong>class CookieConflictError(builtins.RuntimeError)</strong>

     |  There are two cookies that meet the criteria specified in the cookie jar.
     |  Use .get and .set and include domain and path args in order to be more specific.
     |  
     |  Method resolution order:
     |      CookieConflictError
     |      builtins.RuntimeError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.RuntimeError:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.RuntimeError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    

### MockRequest

<strong>class MockRequest(builtins.object)</strong>

     |  MockRequest(request)
     |  
     |  Wraps a `requests.Request` to mimic a `urllib2.Request`.
     |  
     |  The code in `cookielib.CookieJar` expects this interface in order to correctly
     |  manage cookie policies, i.e., determine whether a cookie can be set, given the
     |  domains of the request and the cookie.
     |  
     |  The original request object is read-only. The client is responsible for collecting
     |  the new headers via `get_new_headers()` and interpreting them appropriately. You
     |  probably want `get_cookie_header`, defined below.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, request)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_header(self, key, val)
     |      cookielib has no legitimate use for this method; add it back if you find one.
     |  
     |  add_unredirected_header(self, name, value)
     |  
     |  get_full_url(self)
     |  
     |  get_header(self, name, default=None)
     |  
     |  get_host(self)
     |  
     |  get_new_headers(self)
     |  
     |  get_origin_req_host(self)
     |  
     |  get_type(self)
     |  
     |  has_header(self, name)
     |  
     |  is_unverifiable(self)
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  host
     |  
     |  origin_req_host
     |  
     |  unverifiable
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### MockResponse

<strong>class MockResponse(builtins.object)</strong>

     |  MockResponse(headers)
     |  
     |  Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.
     |  
     |  ...what? Basically, expose the parsed HTTP headers from the server response
     |  the way `cookielib` expects to see them.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, headers)
     |      Make a MockResponse for `cookielib` to read.
     |      
     |      :param headers: a httplib.HTTPMessage or analogous carrying the headers
     |  
     |  getheaders(self, name)
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### RequestsCookieJar

<strong>class RequestsCookieJar(http.cookiejar.CookieJar, collections.abc.MutableMapping)</strong>

     |  RequestsCookieJar(policy=None)
     |  
     |  Compatibility class; is a cookielib.CookieJar, but exposes a dict
     |  interface.
     |  
     |  This is the CookieJar we create by default for requests and sessions that
     |  don't specify one, since some clients may expect response.cookies and
     |  session.cookies to support dict operations.
     |  
     |  Requests does not use the dict interface internally; it's just for
     |  compatibility with external client code. All requests code should work
     |  out of the box with externally provided instances of ``CookieJar``, e.g.
     |  ``LWPCookieJar`` and ``FileCookieJar``.
     |  
     |  Unlike a regular CookieJar, this class is pickleable.
     |  
     |  .. warning:: dictionary operations that are normally O(1) may be O(n).
     |  
     |  Method resolution order:
     |      RequestsCookieJar
     |      http.cookiejar.CookieJar
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
     |  __contains__(self, name)
     |  
     |  __delitem__(self, name)
     |      Deletes a cookie given a name. Wraps ``cookielib.CookieJar``'s
     |      ``remove_cookie_by_name()``.
     |  
     |  __getitem__(self, name)
     |      Dict-like __getitem__() for compatibility with client code. Throws
     |      exception if there are more than one cookie with name. In that case,
     |      use the more explicit get() method instead.
     |      
     |      .. warning:: operation is O(n), not O(1).
     |  
     |  __getstate__(self)
     |      Unlike a normal CookieJar, this class is pickleable.
     |  
     |  __setitem__(self, name, value)
     |      Dict-like __setitem__ for compatibility with client code. Throws
     |      exception if there is already a cookie of that name in the jar. In that
     |      case, use the more explicit set() method instead.
     |  
     |  __setstate__(self, state)
     |      Unlike a normal CookieJar, this class is pickleable.
     |  
     |  copy(self)
     |      Return a copy of this RequestsCookieJar.
     |  
     |  get(self, name, default=None, domain=None, path=None)
     |      Dict-like get() that also supports optional domain and path args in
     |      order to resolve naming collisions from using one cookie jar over
     |      multiple domains.
     |      
     |      .. warning:: operation is O(n), not O(1).
     |  
     |  get_dict(self, domain=None, path=None)
     |      Takes as an argument an optional domain and path and returns a plain
     |      old Python dict of name-value pairs of cookies that meet the
     |      requirements.
     |      
     |      :rtype: dict
     |  
     |  get_policy(self)
     |      Return the CookiePolicy instance used.
     |  
     |  items(self)
     |      Dict-like items() that returns a list of name-value tuples from the
     |      jar. Allows client-code to call ``dict(RequestsCookieJar)`` and get a
     |      vanilla python dict of key value pairs.
     |      
     |      .. seealso:: keys() and values().
     |  
     |  iteritems(self)
     |      Dict-like iteritems() that returns an iterator of name-value tuples
     |      from the jar.
     |      
     |      .. seealso:: iterkeys() and itervalues().
     |  
     |  iterkeys(self)
     |      Dict-like iterkeys() that returns an iterator of names of cookies
     |      from the jar.
     |      
     |      .. seealso:: itervalues() and iteritems().
     |  
     |  itervalues(self)
     |      Dict-like itervalues() that returns an iterator of values of cookies
     |      from the jar.
     |      
     |      .. seealso:: iterkeys() and iteritems().
     |  
     |  keys(self)
     |      Dict-like keys() that returns a list of names of cookies from the
     |      jar.
     |      
     |      .. seealso:: values() and items().
     |  
     |  list_domains(self)
     |      Utility method to list all the domains in the jar.
     |  
     |  list_paths(self)
     |      Utility method to list all the paths in the jar.
     |  
     |  multiple_domains(self)
     |      Returns True if there are multiple domains in the jar.
     |      Returns False otherwise.
     |      
     |      :rtype: bool
     |  
     |  set(self, name, value, **kwargs)
     |      Dict-like set() that also supports optional domain and path args in
     |      order to resolve naming collisions from using one cookie jar over
     |      multiple domains.
     |  
     |  set_cookie(self, cookie, *args, **kwargs)
     |      Set a cookie, without checking whether or not it should be set.
     |  
     |  update(self, other)
     |      Updates this jar with cookies from another CookieJar or dict-like
     |  
     |  values(self)
     |      Dict-like values() that returns a list of values of cookies from the
     |      jar.
     |      
     |      .. seealso:: keys() and items().
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from http.cookiejar.CookieJar:
     |  
     |  __init__(self, policy=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __len__(self)
     |      Return number of contained cookies.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  add_cookie_header(self, request)
     |      Add correct Cookie: header to request (urllib.request.Request object).
     |      
     |      The Cookie2 header is also added unless policy.hide_cookie2 is true.
     |  
     |  clear(self, domain=None, path=None, name=None)
     |      Clear some cookies.
     |      
     |      Invoking this method without arguments will clear all cookies.  If
     |      given a single argument, only cookies belonging to that domain will be
     |      removed.  If given two arguments, cookies belonging to the specified
     |      path within that domain are removed.  If given three arguments, then
     |      the cookie with the specified name, path and domain is removed.
     |      
     |      Raises KeyError if no matching cookie exists.
     |  
     |  clear_expired_cookies(self)
     |      Discard all expired cookies.
     |      
     |      You probably don't need to call this method: expired cookies are never
     |      sent back to the server (provided you're using DefaultCookiePolicy),
     |      this method is called by CookieJar itself every so often, and the
     |      .save() method won't save expired cookies anyway (unless you ask
     |      otherwise by passing a true ignore_expires argument).
     |  
     |  clear_session_cookies(self)
     |      Discard all session cookies.
     |      
     |      Note that the .save() method won't save session cookies anyway, unless
     |      you ask otherwise by passing a true ignore_discard argument.
     |  
     |  extract_cookies(self, response, request)
     |      Extract cookies from response, where allowable given the request.
     |  
     |  make_cookies(self, response, request)
     |      Return sequence of Cookie objects extracted from response object.
     |  
     |  set_cookie_if_ok(self, cookie, request)
     |      Set a cookie if policy says it's OK to do so.
     |  
     |  set_policy(self, policy)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from http.cookiejar.CookieJar:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from http.cookiejar.CookieJar:
     |  
     |  domain_re = re.compile('[^.]*')
     |  
     |  dots_re = re.compile('^\\.+')
     |  
     |  magic_re = re.compile('^\\#LWP-Cookies-(\\d+\\.\\d+)', re.ASCII)
     |  
     |  non_word_re = re.compile('\\W')
     |  
     |  quote_re = re.compile('([\\"\\\\])')
     |  
     |  strict_domain_re = re.compile('\\.?[^.]*')
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
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
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |  
     |  __hash__ = None
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

## Functions

### cookiejar_from_dict

<strong>cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)</strong>
        Returns a CookieJar from a key/value dictionary.
        
        :param cookie_dict: Dict of key/values to insert into CookieJar.
        :param cookiejar: (optional) A cookiejar to add the cookies to.
        :param overwrite: (optional) If False, will not replace cookies
            already in the jar with new ones.
        :rtype: CookieJar
    

### create_cookie

<strong>create_cookie(name, value, **kwargs)</strong>
        Make a cookie from underspecified parameters.
        
        By default, the pair of `name` and `value` will be set for the domain ''
        and sent on every request (this is sometimes called a "supercookie").
    

### extract_cookies_to_jar

<strong>extract_cookies_to_jar(jar, request, response)</strong>
        Extract the cookies from the response into a CookieJar.
        
        :param jar: cookielib.CookieJar (not necessarily a RequestsCookieJar)
        :param request: our own requests.Request object
        :param response: urllib3.HTTPResponse object
    

### get_cookie_header

<strong>get_cookie_header(jar, request)</strong>
        Produce an appropriate Cookie header string to be sent with `request`, or None.
        
        :rtype: str
    

### merge_cookies

<strong>merge_cookies(cookiejar, cookies)</strong>
        Add cookies to cookiejar and returns a merged CookieJar.
        
        :param cookiejar: CookieJar object to add the cookies to.
        :param cookies: Dictionary or CookieJar object to be added.
        :rtype: CookieJar
    

### morsel_to_cookie

<strong>morsel_to_cookie(morsel)</strong>
        Convert a Morsel object into a Cookie containing the one k/v pair.
    

### remove_cookie_by_name

<strong>remove_cookie_by_name(cookiejar, name, domain=None, path=None)</strong>
        Unsets a cookie by name, by default over all domains and paths.
        
        Wraps CookieJar.clear(), is O(n).
