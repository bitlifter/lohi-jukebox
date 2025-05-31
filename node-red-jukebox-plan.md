# Node-RED Jukebox Automation Plan

## Project Goal
Automate a Raspberry Pi Zero 2 W with Node-RED to play an MP3 file (`/home/admin/Music/mystery_unlocked.mp3`) when four specific physical buttons have each been pressed at least once. A fifth physical button will serve as a manual reset for the system.

## Core Components & Logic

1.  **Inputs (Raspberry Pi GPIO):**
    *   Five `rpi-gpio in` nodes will be used:
        *   Button 1 (e.g., GPIO17)
        *   Button 2 (e.g., GPIO27)
        *   Button 3 (e.g., GPIO22)
        *   Button 4 (e.g., GPIO5)
        *   Reset Button (e.g., GPIO6)
    *   **Wiring:** Each switch's COM terminal to Pi GND, NO terminal to the chosen GPIO pin.
    *   **Pull-up Resistors:** Internal pull-up resistors on the Pi will be enabled via the `rpi-gpio in` node configuration. A button press will pull the GPIO pin LOW (0).
    *   **Debouncing:** Each `rpi-gpio in` node will be followed by a `delay` node configured for rate limiting (e.g., 1 message per 100ms) to prevent multiple triggers from switch bounce.

2.  **State Management (Node-RED Flow Context):**
    *   Flow context variables will track the pressed state of the four main buttons:
        *   `flow.button1Pressed` (boolean, default: `false`)
        *   `flow.button2Pressed` (boolean, default: `false`)
        *   `flow.button3Pressed` (boolean, default: `false`)
        *   `flow.button4Pressed` (boolean, default: `false`)
    *   An `inject` node, configured to fire once on deploy/start, will initialize these variables to `false`.

3.  **Button Press Logic (for each of the 4 main buttons):**
    *   After debouncing, the signal from a button press (GPIO pin goes LOW):
        *   A `change` node will set its corresponding flow context variable (e.g., `flow.button1Pressed`) to `true`.
        *   The message will then be passed to a central `function` node responsible for checking the overall state.

4.  **Reset Logic:**
    *   **Manual Reset:**
        *   After debouncing, the signal from the Reset Button press:
        *   A `function` node (or `change` nodes) will set all four flow context variables (`flow.button1Pressed` through `flow.button4Pressed`) back to `false`.
        *   A `debug` node can show a "System Manually Reset" message.
    *   **Automatic Reset (Post-MP3 Playback):** Detailed in section 5.

5.  **"All Buttons Pressed?" Check & MP3 Trigger (`function` node):**
    *   This central `function` node is triggered after any of the four main buttons are pressed and their state is updated.
    *   **Check Condition:** It reads all four flow context variables. If `flow.button1Pressed && flow.button2Pressed && flow.button3Pressed && flow.button4Pressed` are all `true`:
        *   **Trigger MP3:** It constructs a command string (e.g., `mpg123 /home/admin/Music/mystery_unlocked.mp3`).
        *   This command string is sent as `msg.payload` to an `exec` node.
        *   **Automatic Reset:** Immediately after sending the command to the `exec` node, this same `function` node will reset all four flow context variables (`flow.button1Pressed` through `flow.button4Pressed`) back to `false`. This ensures the system is ready for a new sequence and the MP3 plays only once per full set of presses.

6.  **MP3 Playback (`exec` node):**
    *   Receives the command from the `function` node.
    *   Executes the command-line MP3 player (e.g., `mpg123`).
    *   Should be configured to wait for the command to complete if necessary, though for simple playback, this might not be critical.
    *   Output from the `exec` node (stdout, stderr, return code) can be sent to `debug` nodes for troubleshooting.

## Node-RED Flow Summary (Conceptual)

*   **Initialization:** `Inject` node -> `Function` node (set initial flow context variables to false).
*   **Button Inputs (x5):** `rpi-gpio in` -> `Delay` (debounce) -> ...
    *   **Main Buttons (x4):** ... -> `Change` node (set respective `flow.buttonXPressed` to true) -> Central `Function` (Check & Trigger).
    *   **Reset Button (x1):** ... -> `Function` node (set all `flow.buttonXPressed` to false).
*   **Central Logic:** `Function` node (checks all `flow.buttonXPressed`; if all true, sends MP3 command AND resets flow variables).
*   **Output:** Central `Function` node -> `Exec` node (play MP3).
*   **Debugging:** `Debug` nodes attached to various points (e.g., after reset, after MP3 playback).

## Next Steps
Transition to an implementation phase to build this Node-RED flow.