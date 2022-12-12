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

### Status
[panonoctl](https://github.com/florianl/panonoctl) is tested under API version 4.23 with firmware 4.2.873.

### Example Script
A very basic script, which downloads all UPFs from your [PANONO](https://www.panono.com) can be found in [getAllUpfs.py](getAllUpfs.py).

### Connect
```python
>>> from panonoctl import panono
>>> cam = panono()
>>> cam.connect()
```

### Authenticate
```python
>>> cam.auth()
```
You need to authenticate. Otherwise your commands will _not_ be executed.

### Take a Picture
```python
>>> cam.capture()
```

### Get the status of your Panono.
```python
>>> cam.getStatus()
```
Returns a JSON object.

### Get the options of your Panono.
```python
>>> cam.getOptions()
```
Returns a JSON object.

### Get the UPFs (Unstitched Panorama Format) from your Panono.
```python
>>> cam.getUpfs()
```
Returns a JSON object.

### Disconnect
```python
>>> cam.disconnect()
```

### Other Features
[PANONO](https://www.panono.com) provides more features, than those listed above.
If you are interested in trying your own commands take a look [here](Experimental.md) for further information.

License
=======

Copyright 2016 Florian Lehner

Licensed under the Apache License, Version 2.0: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)


# Ethernet over USB
Hello Antoine,

Yes, there are two ways for you to retrieve the raw images off the camera. First, however, I must explain to you that the raw images are zipped together into one file which we call a UPF (Unstitched Panono Format) file. Inside the UPF file are (36 * 4) 144 JPEG images: that is 4 JPEGs corresponding to 3 different color streams (red, green, and blue) for each camera module and there are 36 camera modules. You can use our Panono UPF converter to convert it into 36 individual JPEG images.

To extract the UPF files from the camera, you can use one of the following two methods:
Connect the camera with a computer via USB and transfer the files over MTP.
Communicate with the camera over either WIFI or Ethernet via USB with the camera's API via JSONRPC to programmatically download the files.
(I think you already know this one, but I'll just mention it for sake of completeness) Upload and stitch the images, then download them from our website/backend API.
I'll explain #1 and #2 more below:

Connect the camera with a computer via USB and transfer the files over MTP.
This one is pretty self explanatory. Connect the camera with a computer via a USB-b cord, assuming the camera is in MTP mode (which is the default mode), you can then, depending on the operating system of the computer, find the mounted device and manually copy and paste the files onto your computer.

Communicate with the camera either over WIFI or USB with the camera's API via JSONRPC to programmatically download the files.
I think this one is best explained via some Python code. I'll use this open source Python library as a helper: https://github.com/florianl/panonoctl. And below is simply code I had executed on my computer while in a Python REPL. The '>>>' symbols are the Python interpreter waiting for my input.

First, you must connect your WIFI on your computer to the camera. Make sure the camera is powered on. On your computer, set the WIFI to the Panono device which will be 'Panono-S/N of the camera' where the S/N of the camera is visible on it's outside shell, and the password is right underneath the S/N (if you can't find this, let me know, and I'll send you a picture of it.)

~ $ python
>>> from panonoctl import panono
>>> cam = panono.panono(ip="192.168.80.80",port="42345")
>>> cam.connect()
True
>>> cam.auth()
{"jsonrpc": "2.0", "params": {"device": "test", "force": "test"}, "id": 1, "method": "auth"}
>>> result = cam.experimental("get_upf_infos")
{'jsonrpc': '2.0', 'id': 1, 'result': {'battery_value': -1, 'log_serialize_ready': True, 'auth_token': '3d327e8ca292310510b51e8aac00c0251d9ca55852a9781e31c8cd83e68ebe81920ea13d931735790ab89ff2aa50c87a38f9dfde7aa2370e2ead011b48903dc2', 'power_mode_config': 'eco', 'firmware_version': '6.1.916', 'usb_config': 'network', 'current_time': '2018-11-06 10:22:48,000', 'power_charging_status': 'charging', 'sound_config': 'silent', 'storage': {'panorama': {'usage': 266760192, 'total': 13597483008, 'capacity_available': True}, 'cache': {'usage': 231936000, 'total': 1323102208, 'capacity_available': True}}, 'capture_active': False, 'scheduled_captures': [], 'power_status': 'connected', 'serial_number': 'P6C4AS', 'api_version': '4.54', 'auto_poweroff_count_down': 29.661111332999997, 'is_auth': True, 'capture_available': True, 'update_ready': False, 'charging_status': 'charging', 'accessory': [], 'firmware_update_url': 'http://192.168.10.1:80/update_image', 'capture_locked': False, 'timer_active': False, 'device_id': '19b58e3d52ae50167d1558399bef6de4', 'auto_poweroff_config': True, 'auto_poweroff_timer_config': 30}}
>>> url = result.get('result').get('upf_infos')[0].get('upf_url')
>>> import requests
>>> response = requests.get(url)
>>> file = open("/tmp/some.upf", "w")
>>> file.write(response.content)
>>> file.close()

The port is always 42345 for all our cameras whether using WIFI or Ethernet. The IP address, however, is dependent on whether you can connect via Ethernet or WIFI; it's 192.168.80.80 for WIFI, and it's 192.168.10.1 for ethernet.

To connect via Ethernet over USB you need to folow these steps:

First switch the camera from 'MTP' mode into 'Network' mode; you can do this via either one of the apps: iOS or Android. To find this setting, connect to the camera within the Panono app, then look for the camera settings, there, you will find the switch between either 'MTP' or 'Network' mode.

Next, connect the camera with the USB cord to a computer.

That's it, if you're able to ping 192.168.10.1, you can now communicate with the Panono camera in the same fashion as our apps do.

Thank you,
Nick DeCoursin
