import PyBass.bass as bass_x
import DPG_GUI as dpg_g
import UTF8
def CallBass():
    start_b = bass_x.BASS_INIT(device=-1, freq=48000, flags=0, win=0, dsguid=0)
    if(start_b == False):
        print("Failed to Init BASS")
        exit(122)
    else:
        bass_x.BASS_START()
        bass_stream = bass_x.BASS_StreamCreateFile(mem=0, filename=UTF8.Convert(dpg_g.GetValue_DPG()), offset=0, length=0, flags=0x4)
        bass_x.BASS_ChannelPlay(bass_stream, False)