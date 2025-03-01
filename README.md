# Raspberry-Pi Tank 
This project allows you to control a Raspberry Pi-based tank using a joystick.

## Table of Contents
1. [Setup](#setup)
2. [Hardware Requirements](#hardware-requirements)
3. [Python Libraries](#python-libraries)


### Setup 
On the Raspberry Pi: 

- To determine IP address: ```hostname -I```

- To determine username: ```whoami```

On the Linux OS: 

- To connect to the Raspberry Pi: ```ssh [username]@[IP address]```


### Hardware Requirements 
- Raspberry Pi (any model with GPIO pins)
- Motor driver (L298N or similar)
- Two DC motors
- Joystick controller
- Jumper wires

### Python Libraries
- RPi.GPIO
- Pygame
