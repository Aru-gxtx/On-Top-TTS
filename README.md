# On-Top TTS

**On-Top TTS** is a lightweight, open-source text-to-speech utility designed to stay overlaid on your screen. It allows you to quickly type and broadcast speech without minimizing your full-screen applications or games.

It is specifically designed for users who want to send TTS audio directly into voice chats (Discord, Zoom, In-Game Voice) using a virtual audio cable.

## Features

* **Always on Top:** The window floats over all other applications, including full-screen games.
* **Quick Speak:** Trigger speech by pressing **Enter** or clicking the **Speak** button.
* **Voice Selection:** Automatically detects and lists all installed Windows voice packages.
* **Streamlined Input:** Text box automatically clears new lines on submission for rapid communication.
* **Low Latency:** Uses the native Windows TTS engine for offline, fast performance.

## ⚠️ Audio Routing Setup (Important)

To use this application as a "Microphone" (e.g., to have the TTS speak into Discord or a Game), you must use a **Virtual Audio Cable**.

1.  **Download & Install:** Get a virtual cable driver (e.g., [VB-Audio Virtual Cable](https://vb-audio.com/Cable/)).
2.  **Set Windows Output:**
    * Go to Windows Sound Settings.
    * Set your **Output Device** (Speakers) to **CABLE Input**.
    * *Note: You will stop hearing sound on your speakers temporarily.*
3.  **Set Application Input:**
    * Go to your target app (e.g., Discord > Voice & Video).
    * Set the **Input Device** (Microphone) to **CABLE Output**.
4.  **Hear it Yourself (Optional):**
    * Open Windows Sound Control Panel -> Recording Tab.
    * Right-click **CABLE Output** -> Properties -> Listen Tab.
    * Check "Listen to this device" and select your real speakers/headphones.

## Getting Started

### Prerequisites (For Source Code)

* Python 3.x
* `pyttsx3` library

### Installation

There are two ways to use this program.

### 1. For Users (Recommended)

This is the easiest way to get started. It requires no installation or technical knowledge.

1.  Go to the **Releases** section.
2.  Download the `on_top_tts.exe` file.
3.  Run the file.

### 2. For Developers (Running from Source)

Use this method if you want to run the Python script directly or modify the code.

1.  Clone the repository or download the script.
2.  Install the required dependencies:
    ```bash
    pip install pyttsx3
        *Note: If you encounter errors on Windows, you may also need `pip install pypiwin32`.*
3.  Run the script:
    ```bash
    python always_on_top_tts.py
    
## Usage

1.  **Select Voice:** Use the dropdown menu to select your desired voice (e.g., Microsoft David, Zira, or localized voices).
2.  **Type:** Enter your message in the text box.
3.  **Speak:** Press **Enter** or click **Speak**.

## Adding More Voices (Windows)

If you do not see a specific language in the dropdown:
1.  Go to **Windows Settings** > **Time & Language** > **Speech**.
2.  Under **Manage voices**, click **Add voices**.
3.  Search for the language (e.g., "Filipino") and install it.
4.  Restart On-Top TTS.
