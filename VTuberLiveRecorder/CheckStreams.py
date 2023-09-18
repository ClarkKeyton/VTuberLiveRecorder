import subprocess

class StreamsCheck:
    def GetCMDCommand(nickname : str):
        str_streamlink = 'streamlink'
        livestreams_channels  = 'https://youtube.com/@{}/live'.format(nickname)
        cbb = subprocess.Popen([str_streamlink, livestreams_channels, "best"], shell=False)
        if cbb:
            print("Streamlink Is Opened")