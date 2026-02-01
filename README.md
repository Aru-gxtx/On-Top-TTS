# On-Top TTS (Cloud Edition)

**On-Top Stream TTS** is a lightweight text-to-speech utility designed to stay overlaid on your screen. It allows you to quickly type and broadcast speech without minimizing your full-screen applications or games.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)
![Edge TTS](https://img.shields.io/badge/Engine-Edge%20TTS-blueviolet?style=flat)
![Pygame](https://img.shields.io/badge/Audio-Pygame-yellow?style=flat&logo=python)

## Performance Notice (Important)

**It is highly recommended to run this program from the Python Source (`.py`) rather than the Executable (`.exe`).**

The `.exe` version introduces a delay when connecting to the Cloud TTS servers. Running the Python script directly results in significantly faster response times.

## Features

* **Always on Top:** The window floats over all other applications, including full-screen games.
* **Neural Cloud Voices:** Uses Microsoft Edge's online TTS engine for human-like quality.
* **Two Speaking Modes:**
    * **Instant (Stream):** Speaks automatically every time you press **Space** (for fast, flowing conversation).
    * **Full Sentence:** Waits until you press **Enter** to speak the whole line.
* **Smart Input:** Automatically clears the text box after speaking so you can keep typing.

## Audio Routing Setup

To use this application as a "Microphone", you must use a **Virtual Audio Cable**.

1.  **Download & Install:** Get a virtual cable driver (e.g., [VB-Audio Virtual Cable](https://vb-audio.com/Cable/)).
2.  **Set Output (Where the App Speaks):**
    * Open **Windows Sound Settings** > **App volume and device preferences**.
    * Find **Python** (or `py.exe`) in the list.
    * Set the **Output** to **CABLE Input**.
3.  **Set Input (Where Discord Listens):**
    * Go to your target app (e.g., Discord > Voice & Video).
    * Set the **Input Device** (Microphone) to **CABLE Output**.

*Tip: To hear the voice yourself while it plays to others, go to Windows Sound Control Panel > Recording > CABLE Output > Properties > Listen > Check "Listen to this device".*

## Getting Started

### Prerequisites

* Python 3.x.x installed.
* Internet Connection (Required for Cloud Voices).

### Installation (Recommended Method)

Running from source ensures the fastest TTS response time.

1.  Clone this repository or download the script.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script:
    ```bash
    python on_top_tts.py
    ```

### Installation (Executable Method)

*Note: This method may be slower for Cloud TTS fetching.*

1.  Go to the **Releases** section.
2.  Download `on_top_tts.exe`.
3.  Run the file.

## Usage

1.  **Select Voice:** Choose a voice from the dropdown.
2.  **Select Mode:**
    * **Instant:** Best for gaming. Type a word and hit Space; it speaks immediately.
    * **Full Sentence:** Best for reading prepared text. Type everything, then hit Enter.
3.  **Type & Go:** The text box will clear automatically after sending, keeping you ready for the next word.

## Troubleshooting

* **No Sound?** Check that your Python output is routed to the correct device (Headphones or Cable Input) in Windows Mixer settings.
* **Delay?** Ensure you are running the `.py` file instead of the `.exe`.
