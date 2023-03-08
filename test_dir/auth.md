
# requests.auth

## Description
    

## Classes
    builtins.object
        AuthBase
            HTTPBasicAuth
                HTTPProxyAuth
            HTTPDigestAuth
    

### AuthBase

<strong>class AuthBase(builtins.object)</strong>

     |  Base class that all auth implementations derive from
     |  
     |  Methods defined here:
     |  
     |  __call__(self, r)
     |      Call self as a function.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### HTTPBasicAuth

<strong>class HTTPBasicAuth(AuthBase)</strong>

     |  HTTPBasicAuth(username, password)
     |  
     |  Attaches HTTP Basic Authentication to the given Request object.
     |  
     |  Method resolution order:
     |      HTTPBasicAuth
     |      AuthBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __call__(self, r)
     |      Call self as a function.
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __init__(self, username, password)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ne__(self, other)
     |      Return self!=value.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from AuthBase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### HTTPDigestAuth

<strong>class HTTPDigestAuth(AuthBase)</strong>

     |  HTTPDigestAuth(username, password)
     |  
     |  Attaches HTTP Digest Authentication to the given Request object.
     |  
     |  Method resolution order:
     |      HTTPDigestAuth
     |      AuthBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __call__(self, r)
     |      Call self as a function.
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __init__(self, username, password)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ne__(self, other)
     |      Return self!=value.
     |  
     |  build_digest_header(self, method, url)
     |      :rtype: str
     |  
     |  handle_401(self, r, **kwargs)
     |      Takes the given response and tries digest-auth, if needed.
     |      
     |      :rtype: requests.Response
     |  
     |  handle_redirect(self, r, **kwargs)
     |      Reset num_401_calls counter on redirects.
     |  
     |  init_per_thread_state(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from AuthBase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### HTTPProxyAuth

<strong>class HTTPProxyAuth(HTTPBasicAuth)</strong>

     |  HTTPProxyAuth(username, password)
     |  
     |  Attaches HTTP Proxy Authentication to a given Request object.
     |  
     |  Method resolution order:
     |      HTTPProxyAuth
     |      HTTPBasicAuth
     |      AuthBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __call__(self, r)
     |      Call self as a function.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from HTTPBasicAuth:
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __init__(self, username, password)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ne__(self, other)
     |      Return self!=value.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from HTTPBasicAuth:
     |  
     |  __hash__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from AuthBase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
