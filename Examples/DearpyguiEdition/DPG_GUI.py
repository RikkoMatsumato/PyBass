import dearpygui.dearpygui as dpg
import CallFunc_PyBass
import PyBass.bass as bass
import time
def GetValue(value_tag: str):
    return dpg.get_value(value_tag)
def GetValue_DPG():
    return GetValue("mp3orwav_value")

def StopMusic():
    if(bass.BASSFree()):
        bass.BASSStop()
    else:
        print("Failed to Stop Music or Music is not Played!!!")
        time.sleep(4)
        exit(1443)
def SetupGUI():
    dpg.create_context()
    with dpg.window(label="PyBassDPGExample by RiritoXXL", tag="windowmain", width=555, height=555):
        dpg.add_text("It's Just Example for PyBass(DPG Edition)")
        dpg.add_input_text(label="Mp3 Or WAV Filename", tag="mp3orwav_value")
        dpg.add_button(label="Play Music", callback=CallFunc_PyBass.CallBass)
        dpg.add_button(label="Stop Music", callback=StopMusic)
    dpg.create_viewport(title='PyBass-DPGExample by RiritoXXL', width=555, height=555)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("windowmain", True)
    dpg.start_dearpygui()
    dpg.destroy_context()