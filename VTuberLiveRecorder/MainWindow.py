import GetHashOfVLC
import CheckStreams
import dearpygui.dearpygui as d
import keyboard as k_board
import time
class UI_CheckStreams:
    def CheckStream():
        CheckStreams.StreamsCheck.GetCMDCommand(d.get_value("VtuberNickname"))
    def Main_UI():
        d.create_context()

        with d.window(label="VTuberLiveRecorder", height=755, width=755, tag="VTUBERLIVERECORDER_MAINWINDOW"):
            d.add_input_text(label="Nickname Of VTubers", tag="VtuberNickname")
            d.add_button(label="Check Livestream", callback=UI_CheckStreams.CheckStream)
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
    UI_CheckStreams.Main_UI()
if __name__ == "__main__":
    while True:
        if k_board.is_pressed("X"):
            Main()
        time.sleep(0.4)
    exit(545)