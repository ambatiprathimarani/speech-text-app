from tkinter import *
from tkinter import filedialog, messagebox
from gtts.lang import tts_langs
from text_to_speech import text_to_speech, file_text_to_speech
from speech_to_text import speech_to_text, file_speech_to_text
from file_operations import read_file

# Fetch available languages for gTTS
languages = tts_langs()
language_options = [f"{languages[code]} ({code})" for code in languages]

def setup_ui():
    window = Tk()
    window.geometry("800x600")
    window.title("Speech to Text and Text to Speech Converter")

    # Speech to Text (Microphone)
    stt_frame = LabelFrame(window, text="Speech to Text (Microphone)", padx=10, pady=10)
    stt_frame.place(x=20, y=20, width=350, height=200)

    Label(stt_frame, text="Duration (sec):").grid(row=0, column=0, sticky=W)
    duration_entry = Entry(stt_frame, width=15)
    duration_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(stt_frame, text="Language:").grid(row=1, column=0, sticky=W)
    stt_language_var = StringVar()
    stt_language_var.set(language_options[0])
    stt_language_menu = OptionMenu(stt_frame, stt_language_var, *language_options)
    stt_language_menu.grid(row=1, column=1, padx=10, pady=10)

    def handle_speech_to_text():
        try:
            duration = int(duration_entry.get())
        except ValueError:
            messagebox.showerror(message="Enter a valid duration")
            return
        language_code = stt_language_var.get().split("(")[-1].strip(")")
        result = speech_to_text(duration, language_code)
        if result:
            messagebox.showinfo(message="You said:\n" + result)

    Button(stt_frame, text="Convert Speech to Text", command=handle_speech_to_text).grid(row=2, column=0, columnspan=2, pady=10)

    # Speech to Text (Audio File)
    file_stt_frame = LabelFrame(window, text="Speech to Text (Audio File)", padx=10, pady=10)
    file_stt_frame.place(x=400, y=20, width=350, height=200)

    Label(file_stt_frame, text="Language:").grid(row=0, column=0, sticky=W)
    file_stt_language_var = StringVar()
    file_stt_language_var.set(language_options[0])
    file_stt_language_menu = OptionMenu(file_stt_frame, file_stt_language_var, *language_options)
    file_stt_language_menu.grid(row=0, column=1, padx=10, pady=10)

    def handle_file_speech_to_text():
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if not file_path:
            return
        language_code = file_stt_language_var.get().split("(")[-1].strip(")")
        result = file_speech_to_text(file_path, language_code)
        if result:
            messagebox.showinfo(message="File content transcribed and saved!")

    Button(file_stt_frame, text="Select Audio File", command=handle_file_speech_to_text).grid(row=1, column=0, columnspan=2, pady=10)

    # Text to Speech (Text Input)
    tts_frame = LabelFrame(window, text="Text to Speech (Text Input)", padx=10, pady=10)
    tts_frame.place(x=20, y=250, width=350, height=300)

    Label(tts_frame, text="Text:").grid(row=0, column=0, sticky=W)
    text_entry = Text(tts_frame, width=30, height=8)
    text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    Label(tts_frame, text="Language:").grid(row=2, column=0, sticky=W)
    tts_language_var = StringVar()
    tts_language_var.set(language_options[0])
    tts_language_menu = OptionMenu(tts_frame, tts_language_var, *language_options)
    tts_language_menu.grid(row=2, column=1, padx=10, pady=10)

    def handle_text_to_speech():
        text = text_entry.get("1.0", "end-1c")
        language_code = tts_language_var.get().split("(")[-1].strip(")")
        text_to_speech(text, language_code)

    Button(tts_frame, text="Convert Text to Speech", command=handle_text_to_speech).grid(row=3, column=0, columnspan=2, pady=10)

    # Text to Speech (Text/PDF File)
    file_tts_frame = LabelFrame(window, text="Text to Speech (Text/PDF File)", padx=10, pady=10)
    file_tts_frame.place(x=400, y=250, width=350, height=300)

    Label(file_tts_frame, text="Language:").grid(row=0, column=0, sticky=W)
    file_tts_language_var = StringVar()
    file_tts_language_var.set(language_options[0])
    file_tts_language_menu = OptionMenu(file_tts_frame, file_tts_language_var, *language_options)
    file_tts_language_menu.grid(row=0, column=1, padx=10, pady=10)

    def handle_file_text_to_speech():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if not file_path:
            return
        content = read_file(file_path)
        if content:
            language_code = file_tts_language_var.get().split("(")[-1].strip(")")
            file_text_to_speech(content, language_code)
            messagebox.showinfo(message="Audio file generated and saved!")

    Button(file_tts_frame, text="Select Text/PDF File", command=handle_file_text_to_speech).grid(row=1, column=0, columnspan=2, pady=10)

    # Run the application
    window.mainloop()
