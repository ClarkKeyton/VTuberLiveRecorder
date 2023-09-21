import hashlib
import GetHashOfVLC

class PrintStrHash:
    def PrintStrHashVLC():
        bnn = GetHashOfVLC.getHashOf("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
        return str(bnn.upper())