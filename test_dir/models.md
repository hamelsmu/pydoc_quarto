
# requests.models

## Description
    

## Classes
    builtins.object
        RequestEncodingMixin
            PreparedRequest(RequestEncodingMixin, RequestHooksMixin)
        RequestHooksMixin
            Request
        Response
    

### PreparedRequest

<strong>class PreparedRequest(RequestEncodingMixin, RequestHooksMixin)</strong>

     |  The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
     |  containing the exact bytes that will be sent to the server.
     |  
     |  Instances are generated from a :class:`Request <Request>` object, and
     |  should not be instantiated manually; doing so may produce undesirable
     |  effects.
     |  
     |  Usage::
     |  
     |    >>> import requests
     |    >>> req = requests.Request('GET', 'https://httpbin.org/get')
     |    >>> r = req.prepare()
     |    >>> r
     |    <PreparedRequest [GET]>
     |  
     |    >>> s = requests.Session()
     |    >>> s.send(r)
     |    <Response [200]>
     |  
     |  Method resolution order:
     |      PreparedRequest
     |      RequestEncodingMixin
     |      RequestHooksMixin
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  copy(self)
     |  
     |  prepare(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
     |      Prepares the entire request with the given parameters.
     |  
     |  prepare_auth(self, auth, url='')
     |      Prepares the given HTTP auth data.
     |  
     |  prepare_body(self, data, files, json=None)
     |      Prepares the given HTTP body data.
     |  
     |  prepare_content_length(self, body)
     |      Prepare Content-Length header based on request method and body
     |  
     |  prepare_cookies(self, cookies)
     |      Prepares the given HTTP cookie data.
     |      
     |      This function eventually generates a ``Cookie`` header from the
     |      given cookies using cookielib. Due to cookielib's design, the header
     |      will not be regenerated if it already exists, meaning this function
     |      can only be called once for the life of the
     |      :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
     |      to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
     |      header is removed beforehand.
     |  
     |  prepare_headers(self, headers)
     |      Prepares the given HTTP headers.
     |  
     |  prepare_hooks(self, hooks)
     |      Prepares the given hooks.
     |  
     |  prepare_method(self, method)
     |      Prepares the given HTTP method.
     |  
     |  prepare_url(self, url, params)
     |      Prepares the given HTTP URL.
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from RequestEncodingMixin:
     |  
     |  path_url
     |      Build the path URL to use.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RequestEncodingMixin:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RequestHooksMixin:
     |  
     |  deregister_hook(self, event, hook)
     |      Deregister a previously registered hook.
     |      Returns True if the hook existed, False if not.
     |  
     |  register_hook(self, event, hook)
     |      Properly register a hook.
    

### Request

<strong>class Request(RequestHooksMixin)</strong>

     |  Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
     |  
     |  A user-created :class:`Request <Request>` object.
     |  
     |  Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.
     |  
     |  :param method: HTTP method to use.
     |  :param url: URL to send.
     |  :param headers: dictionary of headers to send.
     |  :param files: dictionary of {filename: fileobject} files to multipart upload.
     |  :param data: the body to attach to the request. If a dictionary or
     |      list of tuples ``[(key, value)]`` is provided, form-encoding will
     |      take place.
     |  :param json: json for the body to attach to the request (if files or data is not specified).
     |  :param params: URL parameters to append to the URL. If a dictionary or
     |      list of tuples ``[(key, value)]`` is provided, form-encoding will
     |      take place.
     |  :param auth: Auth handler or (user, pass) tuple.
     |  :param cookies: dictionary or CookieJar of cookies to attach to this request.
     |  :param hooks: dictionary of callback hooks, for internal usage.
     |  
     |  Usage::
     |  
     |    >>> import requests
     |    >>> req = requests.Request('GET', 'https://httpbin.org/get')
     |    >>> req.prepare()
     |    <PreparedRequest [GET]>
     |  
     |  Method resolution order:
     |      Request
     |      RequestHooksMixin
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  prepare(self)
     |      Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RequestHooksMixin:
     |  
     |  deregister_hook(self, event, hook)
     |      Deregister a previously registered hook.
     |      Returns True if the hook existed, False if not.
     |  
     |  register_hook(self, event, hook)
     |      Properly register a hook.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RequestHooksMixin:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### RequestEncodingMixin

<strong>class RequestEncodingMixin(builtins.object)</strong>

     |  Readonly properties defined here:
     |  
     |  path_url
     |      Build the path URL to use.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### RequestHooksMixin

<strong>class RequestHooksMixin(builtins.object)</strong>

     |  Methods defined here:
     |  
     |  deregister_hook(self, event, hook)
     |      Deregister a previously registered hook.
     |      Returns True if the hook existed, False if not.
     |  
     |  register_hook(self, event, hook)
     |      Properly register a hook.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### Response

<strong>class Response(builtins.object)</strong>

     |  The :class:`Response <Response>` object, which contains a
     |  server's response to an HTTP request.
     |  
     |  Methods defined here:
     |  
     |  __bool__(self)
     |      Returns True if :attr:`status_code` is less than 400.
     |      
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code, is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |  
     |  __enter__(self)
     |  
     |  __exit__(self, *args)
     |  
     |  __getstate__(self)
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |      Allows you to use a response as an iterator.
     |  
     |  __nonzero__(self)
     |      Returns True if :attr:`status_code` is less than 400.
     |      
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code, is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __setstate__(self, state)
     |  
     |  close(self)
     |      Releases the connection back to the pool. Once this method has been
     |      called the underlying ``raw`` object must not be accessed again.
     |      
     |      *Note: Should not normally need to be called explicitly.*
     |  
     |  iter_content(self, chunk_size=1, decode_unicode=False)
     |      Iterates over the response data.  When stream=True is set on the
     |      request, this avoids reading the content at once into memory for
     |      large responses.  The chunk size is the number of bytes it should
     |      read into memory.  This is not necessarily the length of each item
     |      returned as decoding can take place.
     |      
     |      chunk_size must be of type int or None. A value of None will
     |      function differently depending on the value of `stream`.
     |      stream=True will read data as it arrives in whatever size the
     |      chunks are received. If stream=False, data is returned as
     |      a single chunk.
     |      
     |      If decode_unicode is True, content will be decoded using the best
     |      available encoding based on the response.
     |  
     |  iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None)
     |      Iterates over the response data, one line at a time.  When
     |      stream=True is set on the request, this avoids reading the
     |      content at once into memory for large responses.
     |      
     |      .. note:: This method is not reentrant safe.
     |  
     |  json(self, **kwargs)
     |      Returns the json-encoded content of a response, if any.
     |      
     |      :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
     |      :raises requests.exceptions.JSONDecodeError: If the response body does not
     |          contain valid json.
     |  
     |  raise_for_status(self)
     |      Raises :class:`HTTPError`, if one occurred.
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  apparent_encoding
     |      The apparent encoding, provided by the charset_normalizer or chardet libraries.
     |  
     |  content
     |      Content of the response, in bytes.
     |  
     |  is_permanent_redirect
     |      True if this Response one of the permanent versions of redirect.
     |  
     |  is_redirect
     |      True if this Response is a well-formed HTTP redirect that could have
     |      been processed automatically (by :meth:`Session.resolve_redirects`).
     |  
     |  links
     |      Returns the parsed header links of the response, if any.
     |  
     |  next
     |      Returns a PreparedRequest for the next request in a redirect chain, if there is one.
     |  
     |  ok
     |      Returns True if :attr:`status_code` is less than 400, False if not.
     |      
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |  
     |  text
     |      Content of the response, in unicode.
     |      
     |      If Response.encoding is None, encoding will be guessed using
     |      ``charset_normalizer`` or ``chardet``.
     |      
     |      The encoding of the response content is determined based solely on HTTP
     |      headers, following RFC 2616 to the letter. If you can take advantage of
     |      non-HTTP knowledge to make a better guess at the encoding, you should
     |      set ``r.encoding`` appropriately before accessing this property.
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
     |  __attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', '...
