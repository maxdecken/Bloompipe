import os
import subprocess
from shlex import shlex


def convertImgSeqToH264(inPath, outPath, framerate):
    print(os.system("dir"))
    command = "ffmpeg -framerate " + str(framerate) + " -pattern_type sequence -start_number 0001 -i \'" + inPath + "//img%04d.png\' -c:v libx264 -pix_fmt yuv420p \'" + outPath + "/out.mp4\'"
    #os.system("""bin\\ffmpeg\\ffmpeg.exe -framerate 30 -pattern_type sequence -start_number 0001 -i 'C:/Users/maxde/Documents/projectTest/png/LordeTennisCourt%04d.png' -c:v libx264 -pix_fmt yuv420p C:/Users/maxde/Documents/projectTest/out/out.mp4""")
    os.system(command)

#convertImgSeqToH264('/home/max/projectTest/png', '/home/max/projectTest/out', 25)