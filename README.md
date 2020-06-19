# Ping-DPT
Use Ping-Python and pynmea2 to generate Humminbird DPT sentences

# Install from PIP

`pip install Ping-DPT
`

or

`pip install git+https://github.com/NickNothom/Ping-DPT --upgrade
`

or

`git clone https://github.com/NickNothom/Ping-DPT
`

# Usage
You must specify the serial port of your Ping device. The default baud rate is 115200. By default, it will create a log folder in your current directory and store logs there. You can alternatively specify a directory. 

`ping-dpt-logger.py --device /dev/ttyUSB0`

