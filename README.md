# On-Top TTS (Cloud Edition)

**On-Top TTS** is a lightweight text-to-speech utility designed to stay overlaid on your screen. It allows you to quickly type and broadcast speech to voice chats (Discord, Zoom, Games) while hearing it yourself simultaneously—without minimizing your full-screen applications.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)
![Edge TTS](https://img.shields.io/badge/Engine-Edge%20TTS-blueviolet?style=flat)
![SoundDevice](https://img.shields.io/badge/Audio-SoundDevice-ff69b4?style=flat)

## Performance Notice

**It is highly recommended to run this program from the Python Source (`.py`) rather than the Executable (`.exe`).**

The `.exe` version may introduce a slight delay when connecting to the Cloud TTS servers due to packaging overhead. Running the Python script directly results in the fastest response times.

## New Features (Update)

* **🎧 Dual Audio Routing (Splitter):** The app now has **two** output selectors. It plays audio to your speakers (so you hear it) AND to a virtual cable (so they hear it) at the exact same time. No more Windows Mixer hacks!
* **⚡ Speed Control:** Includes a slider to adjust speech speed from -50% (Very Slow) to +50% (Very Fast).
* **🔧 Auto-Resampling:** Automatically detects and fixes sample rate mismatches (e.g., 24kHz vs 48kHz) to prevent crashes and silence.
* **Two Speaking Modes:**
    * **Instant (Stream):** Speaks automatically every time you press **Space**.
    * **Full Sentence:** Waits until you press **Enter** to speak the whole line.

## Audio Setup (How to talk to others)

To use this application as a "Microphone" for Discord/Zoom/Games, you need a **Virtual Audio Cable**.

1.  **Download & Install:** Get a virtual cable driver (e.g., [VB-Audio Virtual Cable](https://vb-audio.com/Cable/)).
2.  **Open the App:**
    * **Dropdown 1 (Your Ears):** Select your actual Headphones/Speakers.
    * **Dropdown 2 (Their Ears):** Select **CABLE Input**.
3.  **Configure Discord/Game:**
    * Go to your target app's settings (Voice & Video).
    * Set the **Input Device (Microphone)** to **CABLE Output**.

## Getting Started

### Prerequisites

* Python 3.x.x installed.
* Internet Connection (Required for Cloud Voices).
* [VB-Cable](https://vb-audio.com/Cable/) (Highly Recommended).

### Installation (Recommended Method)

Running from source ensures the fastest TTS response time.

1.  Clone this repository or download the script.
2.  Install the new dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script:
    ```bash
    python on_top_tts.py
    ```

## Usage

1.  **Select Devices:** Set where you want the sound to go (usually Headphones + Cable Input).
2.  **Select Voice:** Choose a Neural voice from the dropdown.
3.  **Set Speed:** Adjust the slider if you want the voice faster or slower.
4.  **Type & Go:**
    * Use **Space** mode for fast conversation.
    * Use **Enter** mode for prepared sentences.
