Tornado layered router
==============

为Tornado提供类似Django的分层url功能

Usage examples:

```python
    #test/urls.py
    
    from test.views import TestWriteHandle, TestHandle
    urls = [
        (r'write', TestWriteHandle),
        (r'', TestHandle),
    ]
    
    
    #main.py
    
    # coding: utf-8
    from __future__ import unicode_literals
    
    import sys
    import os
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web
    
    from tornado_router import include, url_wrapper
    
    application = tornado.web.Application(url_wrapper([
    (r"/test/", include('test.urls')),
    (r"/write/", include('xxx.urls')),
    (r"/", SomeHandle),
        ]))


    if __name__ == "__main__":
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

```

然后运行:
```
    python main.py
```

访问:
```
    http://localhost:8888/test/write
```
即可看到正确的返回结果