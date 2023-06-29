import speech_recognition as sr
import pyaudio
import numpy as np

def kenali_emosi():
    recognizer = sr.Recognizer()

    # Tetapkan ambang batas untuk tingkat volume untuk mendeteksi emosi
    # ambang_volume = 1001
    
    with sr.Microphone() as source:
        print("Mendengarkan...")
        audio = recognizer.listen(source)

    try:
        print("Mengenali...")
        teks = recognizer.recognize_google(audio, language="id-ID")
        print("Anda mengatakan:", teks)

        # Dapatkan tingkat volume dari data audio
        data_audio = np.frombuffer(audio.frame_data, dtype=np.int16)
        volume = np.abs(data_audio).mean()

        # Tentukan emosi berdasarkan tingkat volume
        if 300 < volume < 500:
            emosi = "Cool"
        elif 501 < volume < 888:
            emosi = "Senang"
        elif 889 < volume < 1100:
            emosi = "Nangis"
        elif volume > 1101:
            emosi = "Marah"
        else:
            emosi = "Tidak beremosi"

        print("Volume:", volume)
        print("Emosi:", emosi)

    except sr.UnknownValueError:
        print("Maaf, tidak dapat memahami audio.")
    except sr.RequestError as e:
        print("Maaf, layanan pengenalan suara tidak tersedia:", str(e))

kenali_emosi()
