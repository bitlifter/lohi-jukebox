# Troubleshooting Guide for Jukebox Escape Room Project

This guide provides solutions for common issues you might encounter when setting up and running the jukebox escape room project.

## Hardware Issues

### Buttons Not Responding

1. **Check Physical Connections**
   - Ensure the COM terminal of each microswitch is connected to a GND pin
   - Ensure the NO terminal of each microswitch is connected to the correct GPIO pin
   - Check for loose connections or broken wires
   - Try using a multimeter to test continuity when the button is pressed

2. **Verify GPIO Pin Numbers**
   - Confirm you're using the correct pin numbering system (BCM vs Physical)
   - In the Node-RED flow, double-check the pin numbers in each "rpi-gpio in" node
   - In the Python test script, verify the pin constants at the top of the file

3. **Test Individual Buttons**
   - Run the `test_gpio_buttons.py` script to check each button individually
   - Press each button and verify that the script detects the press
   - If some buttons work but others don't, focus on the non-working buttons' wiring

4. **GPIO Permissions**
   - Ensure you're running the Python test script with sudo: `sudo python3 test_gpio_buttons.py`
   - For Node-RED, make sure it's running with the correct permissions to access GPIO

## Software Issues

### Node-RED Flow Not Working

1. **Check Node-RED Installation**
   - Verify Node-RED is running: `systemctl status nodered`
   - If not running, start it: `sudo systemctl start nodered`
   - Access the Node-RED editor in a browser: `http://[your-pi-ip]:1880`

2. **Verify Required Nodes**
   - Check if the `node-red-node-pi-gpio` package is installed
   - In Node-RED, go to the menu (≡) > Manage palette > Install tab
   - Search for "node-red-node-pi-gpio" and install if not present

3. **Flow Import Issues**
   - If you encounter errors when importing the flow, try copying the JSON content directly
   - In Node-RED, go to menu (≡) > Import > Clipboard
   - Paste the contents of the `node-red-jukebox-flow.json` file and click Import

4. **Debug the Flow**
   - Enable the debug panel in Node-RED (click the bug icon in the right sidebar)
   - Check for any error messages in the debug panel
   - Verify that messages are flowing through the nodes when buttons are pressed

### Python Test Script Issues

1. **Python Dependencies**
   - Ensure RPi.GPIO is installed: `pip3 list | grep RPi.GPIO`
   - If not installed, run: `sudo pip3 install RPi.GPIO`

2. **Permission Issues**
   - Always run the script with sudo: `sudo python3 test_gpio_buttons.py`
   - Make sure the script is executable: `chmod +x test_gpio_buttons.py`

3. **Script Errors**
   - Check for any error messages when running the script
   - If you see "RuntimeError: Not running on a Raspberry Pi!", ensure you're running on a Raspberry Pi

## MP3 Playback Issues

1. **MP3 Player Installation**
   - Verify mpg123 is installed: `which mpg123`
   - If not installed, run: `sudo apt install -y mpg123`
   - Test mpg123 directly: `mpg123 /home/admin/Music/mystery_unlocked.mp3`

2. **MP3 File Issues**
   - Check if the MP3 file exists: `ls -l /home/admin/Music/mystery_unlocked.mp3`
   - Verify the file permissions: `chmod 644 /home/admin/Music/mystery_unlocked.mp3`
   - Try playing the file manually to check if it works

3. **Audio Output Issues**
   - Ensure the correct audio output is selected: `sudo raspi-config` > System Options > Audio
   - Check the volume: `amixer sset 'Master' 100%`
   - Verify that speakers or headphones are connected and working

4. **Path Issues**
   - If your MP3 file is in a different location, update the path in:
     - Node-RED: "Check All Buttons & Trigger MP3" function node
     - Python script: `MP3_FILE` constant at the top of the file

## Common Errors and Solutions

### "Error: Cannot find module 'node-red-node-pi-gpio'"
- Run: `cd ~/.node-red && npm install node-red-node-pi-gpio`
- Restart Node-RED: `sudo systemctl restart nodered`

### "Error: Command failed: mpg123 /home/admin/Music/mystery_unlocked.mp3"
- Check if mpg123 is installed: `which mpg123`
- Verify the MP3 file exists at the specified path
- Try playing the MP3 file manually to check if it works

### "RuntimeError: This module can only be run on a Raspberry Pi!"
- Ensure you're running the script on a Raspberry Pi
- Check if RPi.GPIO is installed correctly: `sudo pip3 install --upgrade RPi.GPIO`

### "Error: Device or resource busy"
- Another process might be using the GPIO pins
- Restart the Raspberry Pi: `sudo reboot`
- Check for other running scripts that might be using GPIO

### "Error: Not running as root"
- Run the Python script with sudo: `sudo python3 test_gpio_buttons.py`
- For Node-RED, ensure it has the necessary permissions to access GPIO

## Advanced Troubleshooting

### Checking GPIO Status
You can check the current state of GPIO pins using:
```bash
gpio readall
```
Or if gpio is not installed:
```bash
for i in {0..27}; do echo "GPIO$i: $(cat /sys/class/gpio/gpio$i/value 2>/dev/null || echo 'not exported')"; done
```

### Monitoring Node-RED Logs
To see detailed Node-RED logs:
```bash
sudo journalctl -f -u nodered
```

### Testing Button Hardware Without Software
You can use a simple circuit tester or multimeter to test if the buttons are working correctly:
1. Set the multimeter to continuity test mode
2. Connect one probe to the COM terminal and one to the NO terminal
3. When the button is not pressed, there should be no continuity
4. When the button is pressed, there should be continuity

## Getting Help
If you've tried all the troubleshooting steps and still have issues:
1. Take photos of your wiring setup
2. Note any error messages you're seeing
3. Document which steps you've already tried
4. Seek help in Raspberry Pi or Node-RED forums with this detailed information