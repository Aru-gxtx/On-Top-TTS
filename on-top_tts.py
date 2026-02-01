import tkinter as tk
from tkinter import ttk
import threading
import queue
import asyncio
import edge_tts
import pygame
import io
import os

VOICE_OPTIONS = {
    "Filipino (Female) - Blessica": "fil-PH-BlessicaNeural",
    "Filipino (Male) - Angelo": "fil-PH-AngeloNeural",
    "English (Female) - Aria": "en-US-AriaNeural",
    "English (Male) - Guy": "en-US-GuyNeural",
    "English (Female) - Jenny": "en-US-JennyNeural",
    "Japanese (Female) - Nanami": "ja-JP-NanamiNeural",
}

msg_queue = queue.Queue()

def play_audio_data(audio_data):
    try:
        sound_file = io.BytesIO(audio_data)
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        
    except Exception as e:
        print(f"Playback Error: {e}")

async def tts_loop():
    while True:
        try:
            data = await asyncio.to_thread(msg_queue.get)
            if data is None: break # Exit signal
            
            text, voice_short_name = data
            
            communicate = edge_tts.Communicate(text, voice_short_name)
            
            audio_bytes = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_bytes += chunk["data"]
            
            if audio_bytes:
                play_audio_data(audio_bytes)
                
            msg_queue.task_done()
            
        except Exception as e:
            print(f"Cloud TTS Error: {e}")

def start_background_loop():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(tts_loop())

threading.Thread(target=start_background_loop, daemon=True).start()

def get_selected_voice_code():
    name = voice_dropdown.get()
    return VOICE_OPTIONS.get(name, "en-US-AriaNeural")

def handle_space(event):
    if mode_var.get() == "stream":
        text = text_box.get("1.0", tk.END).strip()
        if text:
            msg_queue.put((text, get_selected_voice_code()))
        text_box.delete("1.0", tk.END)
        return "break"
    return None

def handle_enter(event):
    text = text_box.get("1.0", tk.END).strip()
    if text:
        msg_queue.put((text, get_selected_voice_code()))
    text_box.delete("1.0", tk.END)
    return "break"

root = tk.Tk()
root.title("Cloud TTS (Filipino Support)")
root.wm_attributes("-topmost", 1)
root.geometry("380x280")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Voice:").pack(side="left", padx=5)
voice_names = list(VOICE_OPTIONS.keys())
voice_dropdown = ttk.Combobox(frame, values=voice_names, state="readonly", width=30)
voice_dropdown.pack(side="left")
voice_dropdown.current(0) # Default to first

mode_frame = tk.LabelFrame(root, text="Speaking Mode")
mode_frame.pack(pady=5, padx=10, fill="x")

mode_var = tk.StringVar(value="stream")
tk.Radiobutton(mode_frame, text="Instant (Speak on Space)", 
               variable=mode_var, value="stream").pack(anchor="w", padx=10)
tk.Radiobutton(mode_frame, text="Full Sentence (Speak on Enter)", 
               variable=mode_var, value="sentence").pack(anchor="w", padx=10)

tk.Label(root, text="Requires Internet Connection", fg="blue", font=("Arial", 8)).pack(pady=(5, 0))
text_box = tk.Text(root, height=5, width=40, font=("Arial", 12))
text_box.pack(pady=5, padx=10, fill="both", expand=True)

text_box.bind("<Key-space>", handle_space)
text_box.bind("<Return>", handle_enter)

root.mainloop()