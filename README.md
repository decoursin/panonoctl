panonoctl
========

Python API to interact with the [PANONO](https://www.panono.com) 360-camera.

Install
=======

To install, execute:

```
pip install panonoctl
```

Documentation
=============

### Connect
```python
>>> from panonoctl import panono
>>> cam = panono()
>>> cam.connect()
```

### Take a Picture
```python
>>> cam.capture()
```

### Disconnect
```python
>>> cam.disconnect()
```

License
=======

Copyright 2016 Florian Lehner

Licensed under the Apache License, Version 2.0: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)
