import os
import PyBass.bass as bass
import time
import UTF8
from tkinter import filedialog as fd
def Main():
    filenametk = fd.askopenfilename(defaultextension="*.mp3", filetypes=[("MP3 File", "*.mp3"), ("WAV File", "*.wav")])
    print("Filename of This Audio: " + filenametk)
    utf8_filenametk = UTF8.Convert(filenametk)
    bass.BASS_INIT(device=-1, freq=48000, flags=0, win=0, dsguid=0)
    if bass.BASS_START():
        print("BASS IS STARTED SUCCESSFULLY!!!")
        bassstr = bass.BASS_StreamCreateFile(mem=0, filename=utf8_filenametk, offset=0, length=0, flags=0x4)
        bass.BASS_ChannelPlay(handle=bassstr, restart=False)
    else:
        print("Failed to Starting BASS or Audio Device not Founded")
        time.sleep(12)
        os._exit(1178)
    while True:
        time.sleep(43)

if __name__ == "__main__":
    Main()