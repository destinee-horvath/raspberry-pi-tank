# Raspberry-Pi Tank 
This project allows you to control a Raspberry Pi-based tank using a joystick.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/ae3ae672-d46f-4452-b7ae-1f5874b1fb2b" alt="Tank Image 1" width="45%" />
  <img src="https://github.com/user-attachments/assets/c7f55e9b-bfe0-4027-8817-70f47f0aeaeb" alt="Tank Image 2" width="25%" />
</div>

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
