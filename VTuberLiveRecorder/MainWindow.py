import GetHashOfVLC
import CheckStreams
import dearpygui.dearpygui as d
import keyboard as k_board
import time
import ctypes
import PrintStrHash as printx

def SetConsoleTitle(title_name : str):
    return ctypes.cdll.LoadLibrary("Kernel32.dll").SetConsoleTitleW(title_name)
class UI_CheckStreams:
    def CheckStream():
        CheckStreams.StreamsCheck.GetCMDCommand(d.get_value("VtuberNickname"))
    def Download():
        CheckStreams.StreamsCheck.DownloadStreamLive(d.get_value("VtuberNickname"), d.get_value("FilenameMP4"))
    def Main_UI():
        d.create_context()

        with d.window(label="VTuberLiveRecorder", height=755, width=755, tag="VTUBERLIVERECORDER_MAINWINDOW"):
            d.add_input_text(label="Nickname Of VTubers", tag="VtuberNickname", enabled=False)
            d.add_button(label="Check Livestream", callback=UI_CheckStreams.CheckStream)
            d.add_input_text(label="Filename of Current Stream", tag="FilenameMP4")
            d.add_button(label="Download Stream", callback=UI_CheckStreams.Download)
            d.add_text("MD5 Hash Sum of VLC: {}".format(printx.PrintStrHash.PrintStrHashVLC()), color=[215, 55, 75])
        d.create_viewport(title='VTuberLiveRecorder', width=755, height=755)
        d.setup_dearpygui()
        d.show_viewport()
        d.set_primary_window("VTUBERLIVERECORDER_MAINWINDOW", True)
        d.start_dearpygui()
        d.destroy_context()

def Main():
    gethashf = GetHashOfVLC.getHashOf("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
    if gethashf == 'e634616d3b445fc1cd55ee79cf5326ea':
        print("This is Right MD5 Hash Sum")
    else:
        print("Please Download VLC 3.0.18 or Check You're Folder Installation")
        exit(44345)
if __name__ == "__main__":
    SetConsoleTitle("VTuberLiveRecorder by ClarkKeyton")
    Main()
    while True:
        if k_board.is_pressed("X"):
            UI_CheckStreams.Main_UI()
        elif k_board.is_pressed('CTRL+Q'):
            exit(5545)
        time.sleep(0.4)
    exit(545)
