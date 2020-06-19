from setuptools import setup

setup(
    name='Ping-DPT',
    version='0.1',
    packages=['Ping-DPT'],
    install_requires=[
        'pynmea2',
        'bluerobotics-ping',
    ],
    url='https://github.com/NickNothom/Ping-DPT',
    license='MIT',
    author='Nick Nothom',
    author_email='nicknothom@gmail.com',
    description='Output DPT NMEA Sentences from the BlueRobotics Ping Sonar'
)
