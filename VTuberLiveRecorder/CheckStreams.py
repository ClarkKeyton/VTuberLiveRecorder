import subprocess

class StreamsCheck:
    def GetCMDCommand(nickname : str):
        str_streamlink = 'streamlink'
        livestreams_channels  = 'https://youtube.com/@{}/live'.format(nickname)
        cbb = subprocess.Popen([str_streamlink, livestreams_channels, "best"], shell=False)
        if cbb:
            print("Streamlink Is Opened")
    def DownloadStreamLive(nickname : str, name_mp4filename : str):
        str_streamlink = 'streamlink'
        livestreams_channels  = 'https://youtube.com/@{}/live'.format(nickname)
        open_filex = subprocess.Popen([str_streamlink, livestreams_channels, "--hls-live-edge 99999", "--hls-segment-threads 5", "-o" + " {}.mp4".format(name_mp4filename)], shell=False)
        if open_filex:
            print("Streamlink is Now Downloading VTuber's Stream or You're Stream...")
