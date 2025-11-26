import tkinter as tk
from tkinter import ttk # Import ttk for the Combobox (dropdown)
import pyttsx3

try:
    temp_engine = pyttsx3.init()
    voices = temp_engine.getProperty('voices')
    voice_map = {voice.name: voice.id for voice in voices}
    voice_names = list(voice_map.keys())
    del temp_engine
except Exception as e:
    print(f"Error fetching voices: {e}")
    voice_map = {}
    voice_names = ["Default, Microsoft Haruka Desktop - Japanese"]

def speak_text(event=None):
    text_to_speak = text_box.get("1.0", tk.END).strip()
    
    selected_voice_name = voice_dropdown.get()
    
    if text_to_speak:
        try:
            engine = pyttsx3.init()
            
            engine.setProperty('rate', 150) 
            engine.setProperty('volume', 0.9) 
            
            if selected_voice_name in voice_map:
                voice_id = voice_map[selected_voice_name]
                engine.setProperty('voice', voice_id)
            
            engine.say(text_to_speak)
            
            engine.runAndWait()
            
            engine.stop()
            
        except Exception as e:
            print(f"An error occurred: {e}")

    if event:
        return "break"

root = tk.Tk()
root.title("On-Top TTS")

root.wm_attributes("-topmost", 1)

root.geometry("350x250")

voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack(pady=(10, 0))

voice_dropdown = ttk.Combobox(root, values=voice_names, state="readonly", width=40)
voice_dropdown.pack(pady=5)

if voice_names:
    voice_dropdown.current(0)

label = tk.Label(root, text="Enter text below and press 'Speak':")
label.pack(pady=5)

text_box = tk.Text(root, height=5, width=40, wrap="word")
text_box.pack(pady=10, padx=10, fill="x", expand=True)

text_box.bind("<Return>", speak_text)

speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(pady=10)

root.mainloop()
