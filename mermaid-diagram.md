graph TD
    subgraph Initialization
        Inject_Startup[Inject: On Deploy/Start] --> Init_Context{Function: Initialize \n flow.button1Pressed=false \n flow.button2Pressed=false \n flow.button3Pressed=false \n flow.button4Pressed=false};
    end

    subgraph Button Inputs
        B1_GPIO[rpi-gpio in: Button 1] --> B1_Debounce[Delay: Rate Limit \n (e.g., 1 msg/100ms)];
        B2_GPIO[rpi-gpio in: Button 2] --> B2_Debounce[Delay: Rate Limit \n (e.g., 1 msg/100ms)];
        B3_GPIO[rpi-gpio in: Button 3] --> B3_Debounce[Delay: Rate Limit \n (e.g., 1 msg/100ms)];
        B4_GPIO[rpi-gpio in: Button 4] --> B4_Debounce[Delay: Rate Limit \n (e.g., 1 msg/100ms)];
        BR_GPIO[rpi-gpio in: Reset Button] --> BR_Debounce[Delay: Rate Limit \n (e.g., 1 msg/100ms)];
    end

    subgraph State Update & Logic
        B1_Debounce --> B1_Set_True{Change: Set flow.button1Pressed=true};
        B2_Debounce --> B2_Set_True{Change: Set flow.button2Pressed=true};
        B3_Debounce --> B3_Set_True{Change: Set flow.button3Pressed=true};
        B4_Debounce --> B4_Set_True{Change: Set flow.button4Pressed=true};

        B1_Set_True --> Check_All_Buttons{Function: \n Check if all 4 buttons pressed. \n If yes, send msg to Play_MP3 \n AND reset all 4 button states to false.};
        B2_Set_True --> Check_All_Buttons;
        B3_Set_True --> Check_All_Buttons;
        B4_Set_True --> Check_All_Buttons;

        BR_Debounce --> Manual_Reset{Function: \n Reset all 4 button states to false. \n flow.button1Pressed=false \n ... \n flow.button4Pressed=false};
        Manual_Reset --> Reset_Debug[Debug: "System Manually Reset"];
    end

    subgraph MP3 Playback
        Check_All_Buttons -- All True --> Play_MP3_Exec[Exec: mpg123 /home/admin/Music/mystery_unlocked.mp3];
        Play_MP3_Exec --> Playback_Debug[Debug: MP3 Playback Status];
    end

    style Init_Context fill:#lightgrey,stroke:#333,stroke-width:2px
    style B1_Debounce fill:#FFFACD,stroke:#333,stroke-width:1px
    style B2_Debounce fill:#FFFACD,stroke:#333,stroke-width:1px
    style B3_Debounce fill:#FFFACD,stroke:#333,stroke-width:1px
    style B4_Debounce fill:#FFFACD,stroke:#333,stroke-width:1px
    style BR_Debounce fill:#FFFACD,stroke:#333,stroke-width:1px
    style B1_Set_True fill:#lightgreen,stroke:#333,stroke-width:2px
    style B2_Set_True fill:#lightgreen,stroke:#333,stroke-width:2px
    style B3_Set_True fill:#lightgreen,stroke:#333,stroke-width:2px
    style B4_Set_True fill:#lightgreen,stroke:#333,stroke-width:2px
    style Manual_Reset fill:#orange,stroke:#333,stroke-width:2px
    style Check_All_Buttons fill:#lightblue,stroke:#333,stroke-width:4px
    style Play_MP3_Exec fill:#pink,stroke:#333,stroke-width:2px