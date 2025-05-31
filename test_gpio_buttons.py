#!/usr/bin/env python3
"""
GPIO Button Test Script for Jukebox Escape Room Project

This script tests the GPIO connections for the buttons used in the jukebox project.
It monitors the GPIO pins for button presses and plays an MP3 when all buttons have been pressed.

Usage:
    sudo python3 test_gpio_buttons.py
"""

import RPi.GPIO as GPIO
import time
import os
import subprocess

# GPIO pin configuration (BCM numbering)
BUTTON1_PIN = 22  # Physical pin 15
BUTTON2_PIN = 23  # Physical pin 16
BUTTON3_PIN = 24  # Physical pin 18
BUTTON4_PIN = 25  # Physical pin 22
RESET_PIN = 26    # Physical pin 37

# MP3 file path
MP3_FILE = "/home/admin/Music/mystery_unlocked.mp3"

# Button state tracking
button_states = {
    "Button 1": False,
    "Button 2": False,
    "Button 3": False,
    "Button 4": False
}

def setup():
    """Initialize GPIO pins and setup event detection"""
    # Use BCM pin numbering
    GPIO.setmode(GPIO.BCM)
    
    # Setup pins as inputs with pull-up resistors
    GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RESET_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Add event detection for button presses (falling edge = button press with pull-up)
    GPIO.add_event_detect(BUTTON1_PIN, GPIO.FALLING, callback=button1_callback, bouncetime=300)
    GPIO.add_event_detect(BUTTON2_PIN, GPIO.FALLING, callback=button2_callback, bouncetime=300)
    GPIO.add_event_detect(BUTTON3_PIN, GPIO.FALLING, callback=button3_callback, bouncetime=300)
    GPIO.add_event_detect(BUTTON4_PIN, GPIO.FALLING, callback=button4_callback, bouncetime=300)
    GPIO.add_event_detect(RESET_PIN, GPIO.FALLING, callback=reset_callback, bouncetime=300)
    
    print("GPIO setup complete. Monitoring for button presses...")
    print("Press Ctrl+C to exit")

def button1_callback(channel):
    """Callback function for Button 1"""
    button_states["Button 1"] = True
    print("Button 1 pressed!")
    check_all_buttons()

def button2_callback(channel):
    """Callback function for Button 2"""
    button_states["Button 2"] = True
    print("Button 2 pressed!")
    check_all_buttons()

def button3_callback(channel):
    """Callback function for Button 3"""
    button_states["Button 3"] = True
    print("Button 3 pressed!")
    check_all_buttons()

def button4_callback(channel):
    """Callback function for Button 4"""
    button_states["Button 4"] = True
    print("Button 4 pressed!")
    check_all_buttons()

def reset_callback(channel):
    """Callback function for Reset Button"""
    reset_buttons()
    print("Reset button pressed! All button states reset.")

def check_all_buttons():
    """Check if all buttons have been pressed and play MP3 if true"""
    print(f"Current button states: {button_states}")
    
    if all(button_states.values()):
        print("All buttons have been pressed! Playing MP3...")
        play_mp3()
        reset_buttons()

def play_mp3():
    """Play the MP3 file"""
    try:
        # Check if the MP3 file exists
        if not os.path.exists(MP3_FILE):
            print(f"Error: MP3 file not found at {MP3_FILE}")
            return
        
        # Play the MP3 file using mpg123
        subprocess.Popen(["mpg123", MP3_FILE])
        print(f"Playing {MP3_FILE}")
    except Exception as e:
        print(f"Error playing MP3: {e}")

def reset_buttons():
    """Reset all button states to False"""
    for button in button_states:
        button_states[button] = False
    print("Button states reset")

def cleanup():
    """Clean up GPIO resources"""
    GPIO.cleanup()
    print("\nGPIO cleanup complete")

if __name__ == "__main__":
    try:
        setup()
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        cleanup()