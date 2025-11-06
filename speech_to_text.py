import speech_recognition as sr
from tkinter import filedialog, messagebox

def speech_to_text(duration, language_code):
    recorder = sr.Recognizer()
    with sr.Microphone() as mic:
        recorder.adjust_for_ambient_noise(mic)
        try:
            audio_input = recorder.listen(mic, timeout=duration)
            return recorder.recognize_google(audio_input, language=language_code)
        except sr.WaitTimeoutError:
            messagebox.showerror(message="Listening timed out.")
        except sr.UnknownValueError:
            messagebox.showerror(message="Couldn't understand the audio input.")
        except sr.RequestError:
            messagebox.showerror(message="Couldn't request results.")


def file_speech_to_text(file_path, language_code):
    recorder = sr.Recognizer()
    with sr.AudioFile(file_path) as audio_file:
        audio_data = recorder.record(audio_file)
        try:
            result = recorder.recognize_google(audio_data, language=language_code)
            # Let the user choose where to save the text
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="Save Transcribed Text"
            )
            if save_path:
                with open(save_path, "w") as file:
                    file.write(result)
                messagebox.showinfo(message=f"Transcription saved to {save_path}")
            return result
        except sr.UnknownValueError:
            messagebox.showerror(message="Couldn't understand the audio.")
        except sr.RequestError:
            messagebox.showerror(message="Couldn't request results.")


