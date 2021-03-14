Some scripts to access the data streamed by the **Neurosky Mindwave Mobile** Headset over Bluetooth on Linux.

Requirements:
* [PyBluez](http://code.google.com/p/pybluez/), see their [documentation](http://code.google.com/p/pybluez/wiki/Documentation) for installation instructions :)
For Ubuntu, installation might work like this:
```
sudo apt-get install libbluetooth-dev python-bluetooth
```

If you want to install the library as a module, do:
```
python3 setup.py install
```
from the root folder of the repository.

example code:
	python3 read_mindwave_mobile.py rgb_test --addr 1D:3D:3E:9E:6G:3H
	
	usage: read_mindwave_mobile.py [-h] [--addr DEVICEADDR]
        	                       dataLabel [dataLabel ...]
