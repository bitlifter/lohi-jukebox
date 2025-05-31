#!/bin/bash
# Installation script for Jukebox Escape Room Project
# This script installs all necessary dependencies for both the Node-RED flow and Python test script

echo "===== Jukebox Escape Room Project Setup ====="
echo "This script will install all necessary dependencies."
echo "It requires sudo privileges for some operations."
echo ""

# Check if running as root/sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo:"
  echo "sudo ./setup.sh"
  exit 1
fi

echo "===== Updating package lists ====="
apt update

echo ""
echo "===== Installing mpg123 (MP3 player) ====="
apt install -y mpg123

echo ""
echo "===== Installing Python dependencies ====="
apt install -y python3-pip python3-rpi.gpio

echo ""
echo "===== Installing Node-RED GPIO nodes ====="
# Check if Node-RED is installed
if [ -d "/home/$(logname)/.node-red" ]; then
  cd /home/$(logname)/.node-red
  echo "Installing node-red-node-pi-gpio..."
  sudo -u $(logname) npm install node-red-node-pi-gpio
else
  echo "Node-RED directory not found. Please install Node-RED first."
  echo "You can install Node-RED using the following command:"
  echo "bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)"
fi

echo ""
echo "===== Making test script executable ====="
chmod +x test_gpio_buttons.py

echo ""
echo "===== Setup Complete ====="
echo ""
echo "To test your GPIO setup, run:"
echo "sudo python3 test_gpio_buttons.py"
echo ""
echo "To import the Node-RED flow:"
echo "1. Open Node-RED in your browser (typically at http://[your-pi-ip]:1880)"
echo "2. Click the menu button (≡) in the top-right corner"
echo "3. Select 'Import' from the menu"
echo "4. Click 'select a file to import'"
echo "5. Navigate to and select the node-red-jukebox-flow.json file"
echo "6. Click 'Import'"
echo ""
echo "For more information, see the README.md file."