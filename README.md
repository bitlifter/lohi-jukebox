gh2-lohi-jukebox
================

### About

This is your project's README.md file. It helps users understand what your
project does, how to use it and anything else they may need to know.
=======
# Jukebox Escape Room Project

This project automates a 1953 EMI jukebox for an escape room art installation using a Raspberry Pi Zero 2 W running Node-RED.

## Overview

When each of four physical buttons is pressed at least once, the system plays an MP3 file. A fifth button acts as a manual reset. The system also automatically resets after successful MP3 playback.

## Prerequisites

1. **Hardware**:
   - Raspberry Pi Zero 2 W
   - 5× 1185RE8 microswitches (4 for input, 1 for reset)
   - Wiring (jumper wires, breadboard if needed)

2. **Software**:
   - Raspberry Pi OS
   - Node-RED 4.0.9 or compatible
   - `node-red-node-pi-gpio` package (for GPIO access)
   - Command-line MP3 player (e.g., `mpg123`)

## Installation

### 1. Install Required Software

If not already installed, install the required software on your Raspberry Pi:

```bash
# Update package lists
sudo apt update

# Install mpg123 (MP3 player)
sudo apt install -y mpg123

# Install Node-RED GPIO nodes (if not already installed)
cd ~/.node-red
npm install node-red-node-pi-gpio
```

### 2. Import the Flow

1. Open Node-RED in your browser (typically at `http://[your-pi-ip]:1880`)
2. Click the menu button (≡) in the top-right corner
3. Select "Import" from the menu
4. Click "select a file to import"
5. Navigate to and select the `node-red-jukebox-flow.json` file
6. Click "Import"

### 3. Configure GPIO Pins (if needed)

The flow is pre-configured with the following GPIO pins (BCM numbering):
- Button 1: GPIO22 (Physical pin 15)
- Button 2: GPIO23 (Physical pin 16)
- Button 3: GPIO24 (Physical pin 18)
- Button 4: GPIO25 (Physical pin 22)
- Reset Button: GPIO26 (Physical pin 37)

If you need to use different pins:
1. Double-click on each "rpi-gpio in" node
2. Change the pin number as needed
3. Click "Done"

### 4. Deploy the Flow

1. Click the "Deploy" button in the top-right corner of the Node-RED interface
2. The flow will be activated and the button states will be initialized

## Wiring Instructions

For each button (using internal pull-up resistors):
1. Connect the COM terminal of the microswitch to a GND pin on the Raspberry Pi
2. Connect the NO terminal of the microswitch to the appropriate GPIO pin

Example wiring diagram for one button:
```
Raspberry Pi GPIO Pin (e.g., GPIO17) ---- NO Terminal of Microswitch
Raspberry Pi Ground (GND) Pin       ---- COM Terminal of Microswitch
```

## Testing

1. Open the Node-RED debug panel (click the bug icon in the right sidebar)
2. Press each button individually and verify that the debug panel shows the button press
3. After pressing all four main buttons, the MP3 should play and the system should reset
4. Press the reset button to manually reset the system

## Troubleshooting

### Button Presses Not Detected
- Check wiring connections
- Verify GPIO pin numbers in Node-RED match your physical connections
- Ensure the `node-red-node-pi-gpio` package is installed
- Try increasing the debounce time in the "rpi-gpio in" nodes

### MP3 Not Playing
- Verify that `mpg123` is installed: `which mpg123`
- Check that the MP3 file exists at `/home/admin/Music/mystery_unlocked.mp3`
- If using a different path, update the "Check All Buttons & Trigger MP3" function node

### System Not Resetting
- Check the debug panel for error messages
- Verify that the flow context variables are being set correctly

## Customization

### Changing the MP3 File
1. Double-click the "Check All Buttons & Trigger MP3" function node
2. Change the file path in the line: `msg.payload = "mpg123 /home/admin/Music/mystery_unlocked.mp3";`
3. Click "Done" and deploy the changes

### Adjusting Debounce Settings
1. Double-click any "Debounce" delay node
2. Modify the rate limit settings (default is 1 message per second)
3. Click "Done" and deploy the changes
