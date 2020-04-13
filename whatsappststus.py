from moviepy.editor import VideoFileClip, concatenate_videoclips

import os

path = "/home/cyberhunter/Videos/fask app"
filename = "2020-03-30 02-21-51.mp4"
fileobj = "/home/cyberhunter/Videos/fask app/2020-03-30 02-21-51.mp4"
clip1 = VideoFileClip(fileobj)

os.chdir(path)
if not os.path.exists('processed'):
    os.mkdir('processed')

for i in range(0, int(clip1.duration), 15):

    if not clip1.duration < i+15:
        clip2 = VideoFileClip(fileobj).subclip(i, i+15)
    else:
        clip2 = VideoFileClip(fileobj).subclip(i, clip1.duration)

    clip2.write_videofile(f"{path}/processed/{(i//15+1)}_{filename}")
    print(f"Clip {i//15} is processed")