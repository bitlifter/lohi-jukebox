# Project Structure

This document explains the organization and purpose of each file in the Jukebox Escape Room project.

## Overview

```
jukebox-escape-room/
├── node-red-jukebox-flow.json   # Node-RED flow definition (import into Node-RED)
├── test_gpio_buttons.py         # Python script for testing GPIO connections
├── setup.sh                     # Installation script for dependencies
├── README.md                    # Main documentation and setup instructions
├── TROUBLESHOOTING.md           # Detailed troubleshooting guide
├── wiring_diagram.txt           # Text-based wiring diagram
├── mermaid-diagram.md           # Visual flow diagram (Mermaid format)
├── node-red-jukebox-plan.md     # Detailed project plan
└── .roo-context.md              # Project context and status
```

## File Descriptions

### Implementation Files

1. **`node-red-jukebox-flow.json`**
   - The main Node-RED flow definition
   - Import this file into Node-RED to implement the jukebox automation
   - Contains all nodes and connections for the complete solution

2. **`test_gpio_buttons.py`**
   - Python script for testing GPIO connections
   - Use this to verify your hardware setup before implementing the Node-RED flow
   - Monitors button presses and plays the MP3 file when all buttons are pressed

3. **`setup.sh`**
   - Bash script to install all necessary dependencies
   - Installs mpg123, Python GPIO libraries, and Node-RED nodes
   - Makes the test script executable

### Documentation Files

4. **`README.md`**
   - Main documentation file
   - Contains setup instructions, prerequisites, and usage information
   - First file to read when starting the project

5. **`TROUBLESHOOTING.md`**
   - Detailed troubleshooting guide
   - Solutions for common hardware and software issues
   - Reference when encountering problems

6. **`wiring_diagram.txt`**
   - Text-based wiring diagram
   - Shows how to connect the microswitches to the Raspberry Pi GPIO pins
   - Includes pin mappings and connection instructions

### Planning and Design Files

7. **`mermaid-diagram.md`**
   - Visual representation of the Node-RED flow
   - Shows the logical connections between nodes
   - Useful for understanding the flow structure

8. **`node-red-jukebox-plan.md`**
   - Detailed project plan
   - Explains the logic and components of the solution
   - Provides technical details about the implementation

9. **`.roo-context.md`**
   - Project context and status
   - Overview of completed work and next steps
   - Helps track project progress

## Usage Workflow

1. **Setup**:
   - Run `setup.sh` to install dependencies
   - Follow wiring instructions in `wiring_diagram.txt`

2. **Testing**:
   - Run `test_gpio_buttons.py` to verify GPIO connections
   - Troubleshoot any issues using `TROUBLESHOOTING.md`

3. **Implementation**:
   - Import `node-red-jukebox-flow.json` into Node-RED
   - Deploy the flow and test the complete solution

4. **Reference**:
   - Refer to `README.md` for general information
   - Use `TROUBLESHOOTING.md` for resolving issues
   - Consult `node-red-jukebox-plan.md` for technical details