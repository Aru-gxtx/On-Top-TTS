import tkinter as tk
from tkinter import ttk
import threading
import queue
import asyncio
import edge_tts
import sounddevice as sd
import soundfile as sf
import numpy as np
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

def resample_audio(data, original_rate, target_rate):
    """Resamples audio data using linear interpolation to match target device rate."""
    if original_rate == target_rate:
        return data
    
    duration = len(data) / original_rate
    target_length = int(duration * target_rate)
    
    x_old = np.linspace(0, len(data), num=len(data))
    x_new = np.linspace(0, len(data), num=target_length)
    
    if len(data.shape) > 1 and data.shape[1] > 1:
        left = np.interp(x_new, x_old, data[:, 0])
        right = np.interp(x_new, x_old, data[:, 1])
        return np.column_stack((left, right)).astype(np.float32)
    else:
        return np.interp(x_new, x_old, data).astype(np.float32)

def get_audio_devices():
    devices = sd.query_devices()
    device_list = []
    for i, dev in enumerate(devices):
        if dev['max_output_channels'] > 0:
            name = f"{i}: {dev['name']}"
            device_list.append(name)
    return device_list

def play_audio_dual(filename, primary_idx, secondary_idx):
    try:
        file_data, file_rate = sf.read(filename)
        
        def play_stream(device_idx, source_data, source_rate):
            try:
                if device_idx is None: return

                try:
                    dev_info = sd.query_devices(device_idx)
                    target_rate = int(dev_info['default_samplerate'])
                except:
                    target_rate = 44100 

                if source_rate != target_rate:
                    final_data = resample_audio(source_data, source_rate, target_rate)
                else:
                    final_data = source_data
                
                sd.play(final_data, target_rate, device=device_idx)
                sd.wait()
                
            except Exception as e:
                print(f"Stream Error on Device {device_idx}: {e}")

        t1 = threading.Thread(target=play_stream, args=(primary_idx, file_data, file_rate))
        t2 = threading.Thread(target=play_stream, args=(secondary_idx, file_data, file_rate))
        
        t1.start()
        t2.start()
        t1.join()
        t2.join()
            
    except Exception as e:
        print(f"Global Playback Error: {e}")

async def tts_loop():
    while True:
        try:
            data = await asyncio.to_thread(msg_queue.get)
            if data is None: break 
            
            text, voice_code, rate_str, primary_id, secondary_id = data
            
            communicate = edge_tts.Communicate(text, voice_code, rate=rate_str)
            temp_filename = "temp_voice.mp3"
            await communicate.save(temp_filename)
            
            if os.path.exists(temp_filename) and os.path.getsize(temp_filename) > 0:
                play_audio_dual(temp_filename, primary_id, secondary_id)
                try:
                    os.remove(temp_filename)
                except:
                    pass
            
            msg_queue.task_done()
            
        except Exception as e:
            print(f"TTS Loop Error: {e}")

def start_background_service():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(tts_loop())

threading.Thread(target=start_background_service, daemon=True).start()

def get_device_index(combobox):
    selection = combobox.get()
    if selection:
        return int(selection.split(":")[0])
    return None

def send_to_queue():
    text = text_box.get("1.0", tk.END).strip()
    voice = VOICE_OPTIONS.get(voice_dropdown.get(), "en-US-AriaNeural")
    dev1 = get_device_index(device_dropdown_1)
    dev2 = get_device_index(device_dropdown_2)
    
    speed_val = int(speed_slider.get())
    rate_str = f"{speed_val:+d}%"

    if text:
        msg_queue.put((text, voice, rate_str, dev1, dev2))
        text_box.delete("1.0", tk.END)

def handle_key(event):
    if mode_var.get() == "enter":
        send_to_queue()
        return "break"
    return None

def handle_space(event):
    if mode_var.get() == "space":
        send_to_queue()
        return "break"
    return None

root = tk.Tk()
root.title("Dual TTS (Fixed + Speed Control)")
root.geometry("400x520") # Made taller for slider

all_devices = get_audio_devices()

tk.Label(root, text="1. Your Speakers", font=("Arial", 9, "bold")).pack(pady=(10,0))
device_dropdown_1 = ttk.Combobox(root, values=all_devices, state="readonly", width=50)
device_dropdown_1.pack(pady=5)
if all_devices: device_dropdown_1.current(0)

tk.Label(root, text="2. CABLE Input (For Others)", font=("Arial", 9, "bold")).pack(pady=(10,0))
device_dropdown_2 = ttk.Combobox(root, values=all_devices, state="readonly", width=50)
device_dropdown_2.pack(pady=5)
for i, dev in enumerate(all_devices):
    if "CABLE Input" in dev:
        device_dropdown_2.current(i)

tk.Label(root, text="3. Select Voice", font=("Arial", 9, "bold")).pack(pady=(10,0))
voice_dropdown = ttk.Combobox(root, values=list(VOICE_OPTIONS.keys()), state="readonly", width=50)
voice_dropdown.pack(pady=5)
voice_dropdown.current(0)

tk.Label(root, text="4. Speech Speed", font=("Arial", 9, "bold")).pack(pady=(10,0))
speed_slider = tk.Scale(root, from_=-50, to=50, orient="horizontal", length=300, label="Speed %")
speed_slider.set(-25)
speed_slider.pack(pady=0)

mode_frame = tk.LabelFrame(root, text="Activation Mode")
mode_frame.pack(pady=10, fill="x", padx=10)
mode_var = tk.StringVar(value="enter")
tk.Radiobutton(mode_frame, text="Speak on ENTER", variable=mode_var, value="enter").pack(side="left", padx=20)
tk.Radiobutton(mode_frame, text="Speak on SPACE", variable=mode_var, value="space").pack(side="left", padx=20)

text_box = tk.Text(root, height=5, width=40, font=("Arial", 12))
text_box.pack(pady=10, padx=10, expand=True, fill="both")
text_box.bind("<Return>", handle_key)
text_box.bind("<space>", handle_space)

root.mainloop()