Create your own Command
=======================

To provide an easy way, to try your own command on your [PANONO](https://www.panono.com)
there is another command you can use.

### Experimental
```python
>>> result = cam.experimental("status_update")
```

`experimental()` takes at least one argument. The command you want to send
your [PANONO](https://www.panono.com).
In addition you can provide an optional second argument, which must be a json-object, 
to `experimental()`.
`experimental()` always returns a json-object. If your [PANONO](https://www.panono.com)
does not like to execute your command, you will get an error message.
