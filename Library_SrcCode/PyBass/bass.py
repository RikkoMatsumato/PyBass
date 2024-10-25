import ctypes
import os

BASS_LOOP = int(0x4)
def GetMainDLL():
    try:
        dllpath = os.path.join(os.path.dirname(__file__), 'x64_bass\\bass.dll')
        bassdll = ctypes.cdll.LoadLibrary(dllpath)
        return bassdll
    except:
        raise RuntimeError("Not Founded bass.dll or not installed Visual C++ Runtime All-in-One and DirectX... \nPlease Restart PC after Installing This!!!")
def BASS_INIT(device : ctypes.c_int, freq : ctypes.c_int32, flags : ctypes.c_int32, win : ctypes.c_int, dsguid : ctypes.c_int) -> ctypes.c_bool:
    GetMainDLL().BASS_Init.restype = ctypes.c_bool
    GetMainDLL().BASS_Init.argtypes = [ctypes.c_int, ctypes.c_int32, ctypes.c_int32, ctypes.c_int, ctypes.c_int]
    return GetMainDLL().BASS_Init(device, freq, flags, win, dsguid)
def BASSFree() -> ctypes.c_bool:
    GetMainDLL().BASS_Free.restype = ctypes.c_bool
    return GetMainDLL().BASS_Free()
def BASSStop() -> ctypes.c_bool:
    GetMainDLL().BASS_Stop.restype = ctypes.c_bool
    return GetMainDLL().BASS_Stop()
def BASS_StreamCreateFile(mem : ctypes.c_int, filename : ctypes.c_char, offset : ctypes.c_int, length : ctypes.c_int, flags : ctypes.c_int) -> ctypes.c_ulong:
    GetMainDLL().BASS_StreamCreateFile.restype = ctypes.c_ulong
    GetMainDLL().BASS_StreamCreateFile.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    return GetMainDLL().BASS_StreamCreateFile(mem, filename, offset, length, flags)
def BASS_START() -> ctypes.c_bool:
    return GetMainDLL().BASS_Start()
def BASS_ChannelPlay(handle : int, restart : bool) -> ctypes.c_int:
    return GetMainDLL().BASS_ChannelPlay(handle, restart)
