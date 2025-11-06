from gtts import gTTS
import os
from tkinter import filedialog, messagebox

def text_to_speech(text, language_code):
    if not text or not language_code:
        messagebox.showerror(message="Enter required details")
        return
    # Let the user choose where to save the audio file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("Audio Files", "*.mp3")],
        title="Save Speech Audio File"
    )
    if save_path:
        speech = gTTS(text=text, lang=language_code, slow=False)
        speech.save(save_path)
        messagebox.showinfo(message=f"Audio file saved to {save_path}")
        # Optionally, play the audio
        os.system(f"start {save_path}" if os.name == "nt" else f"mpg123 {save_path}")



def file_text_to_speech(content, language_code):
    if not content or not language_code:
        messagebox.showerror(message="Enter required details")
        return
    # Let the user choose where to save the audio file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("Audio Files", "*.mp3")],
        title="Save Speech Audio File"
    )
    if save_path:
        speech = gTTS(text=content, lang=language_code, slow=False)
        speech.save(save_path)
        messagebox.showinfo(message=f"Audio file saved to {save_path}")
        # Optionally, play the audio
        os.system(f"start {save_path}" if os.name == "nt" else f"mpg123 {save_path}")
