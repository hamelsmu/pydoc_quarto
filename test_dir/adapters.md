
# requests.adapters

## Description
    

## Classes
    builtins.object
        BaseAdapter
            HTTPAdapter
    

### BaseAdapter

<strong>class BaseAdapter(builtins.object)</strong>

     |  The Base Transport Adapter
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  close(self)
     |      Cleans up adapter specific items.
     |  
     |  send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)
     |      Sends PreparedRequest object. Returns Response object.
     |      
     |      :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
     |      :param stream: (optional) Whether to stream the request content.
     |      :param timeout: (optional) How long to wait for the server to send
     |          data before giving up, as a float, or a :ref:`(connect timeout,
     |          read timeout) <timeouts>` tuple.
     |      :type timeout: float or tuple
     |      :param verify: (optional) Either a boolean, in which case it controls whether we verify
     |          the server's TLS certificate, or a string, in which case it must be a path
     |          to a CA bundle to use
     |      :param cert: (optional) Any user-provided SSL certificate to be trusted.
     |      :param proxies: (optional) The proxies dictionary to apply to the request.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    

### HTTPAdapter

<strong>class HTTPAdapter(BaseAdapter)</strong>

     |  HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)
     |  
     |  The built-in HTTP Adapter for urllib3.
     |  
     |  Provides a general-case interface for Requests sessions to contact HTTP and
     |  HTTPS urls by implementing the Transport Adapter interface. This class will
     |  usually be created by the :class:`Session <Session>` class under the
     |  covers.
     |  
     |  :param pool_connections: The number of urllib3 connection pools to cache.
     |  :param pool_maxsize: The maximum number of connections to save in the pool.
     |  :param max_retries: The maximum number of retries each connection
     |      should attempt. Note, this applies only to failed DNS lookups, socket
     |      connections and connection timeouts, never to requests where data has
     |      made it to the server. By default, Requests does not retry failed
     |      connections. If you need granular control over the conditions under
     |      which we retry a request, import urllib3's ``Retry`` class and pass
     |      that instead.
     |  :param pool_block: Whether the connection pool should block for connections.
     |  
     |  Usage::
     |  
     |    >>> import requests
     |    >>> s = requests.Session()
     |    >>> a = requests.adapters.HTTPAdapter(max_retries=3)
     |    >>> s.mount('http://', a)
     |  
     |  Method resolution order:
     |      HTTPAdapter
     |      BaseAdapter
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __setstate__(self, state)
     |  
     |  add_headers(self, request, **kwargs)
     |      Add any headers needed by the connection. As of v2.0 this does
     |      nothing by default, but is left for overriding by users that subclass
     |      the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      This should not be called from user code, and is only exposed for use
     |      when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param request: The :class:`PreparedRequest <PreparedRequest>` to add headers to.
     |      :param kwargs: The keyword arguments from the call to send().
     |  
     |  build_response(self, req, resp)
     |      Builds a :class:`Response <requests.Response>` object from a urllib3
     |      response. This should not be called from user code, and is only exposed
     |      for use when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`
     |      
     |      :param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
     |      :param resp: The urllib3 response object.
     |      :rtype: requests.Response
     |  
     |  cert_verify(self, conn, url, verify, cert)
     |      Verify a SSL certificate. This method should not be called from user
     |      code, and is only exposed for use when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param conn: The urllib3 connection object associated with the cert.
     |      :param url: The requested URL.
     |      :param verify: Either a boolean, in which case it controls whether we verify
     |          the server's TLS certificate, or a string, in which case it must be a path
     |          to a CA bundle to use
     |      :param cert: The SSL certificate to verify.
     |  
     |  close(self)
     |      Disposes of any internal state.
     |      
     |      Currently, this closes the PoolManager and any active ProxyManager,
     |      which closes any pooled connections.
     |  
     |  get_connection(self, url, proxies=None)
     |      Returns a urllib3 connection for the given URL. This should not be
     |      called from user code, and is only exposed for use when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param url: The URL to connect to.
     |      :param proxies: (optional) A Requests-style dictionary of proxies used on this request.
     |      :rtype: urllib3.ConnectionPool
     |  
     |  init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs)
     |      Initializes a urllib3 PoolManager.
     |      
     |      This method should not be called from user code, and is only
     |      exposed for use when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param connections: The number of urllib3 connection pools to cache.
     |      :param maxsize: The maximum number of connections to save in the pool.
     |      :param block: Block when no free connections are available.
     |      :param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
     |  
     |  proxy_headers(self, proxy)
     |      Returns a dictionary of the headers to add to any request sent
     |      through a proxy. This works with urllib3 magic to ensure that they are
     |      correctly sent to the proxy, rather than in a tunnelled request if
     |      CONNECT is being used.
     |      
     |      This should not be called from user code, and is only exposed for use
     |      when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param proxy: The url of the proxy being used for this request.
     |      :rtype: dict
     |  
     |  proxy_manager_for(self, proxy, **proxy_kwargs)
     |      Return urllib3 ProxyManager for the given proxy.
     |      
     |      This method should not be called from user code, and is only
     |      exposed for use when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param proxy: The proxy to return a urllib3 ProxyManager for.
     |      :param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
     |      :returns: ProxyManager
     |      :rtype: urllib3.ProxyManager
     |  
     |  request_url(self, request, proxies)
     |      Obtain the url to use when making the final request.
     |      
     |      If the message is being sent through a HTTP proxy, the full URL has to
     |      be used. Otherwise, we should only use the path portion of the URL.
     |      
     |      This should not be called from user code, and is only exposed for use
     |      when subclassing the
     |      :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.
     |      
     |      :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
     |      :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
     |      :rtype: str
     |  
     |  send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)
     |      Sends PreparedRequest object. Returns Response object.
     |      
     |      :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
     |      :param stream: (optional) Whether to stream the request content.
     |      :param timeout: (optional) How long to wait for the server to send
     |          data before giving up, as a float, or a :ref:`(connect timeout,
     |          read timeout) <timeouts>` tuple.
     |      :type timeout: float or tuple or urllib3 Timeout object
     |      :param verify: (optional) Either a boolean, in which case it controls whether
     |          we verify the server's TLS certificate, or a string, in which case it
     |          must be a path to a CA bundle to use
     |      :param cert: (optional) Any user-provided SSL certificate to be trusted.
     |      :param proxies: (optional) The proxies dictionary to apply to the request.
     |      :rtype: requests.Response
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __attrs__ = ['max_retries', 'config', '_pool_connections', '_pool_maxs...
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseAdapter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
