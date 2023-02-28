'''
install pytube using pip install pytube3
'''

from pytube import YouTube

url='Your Video URL'

my_video = YouTube(url)

my_video = my_video.streams.get_highest_resolution()

my_video.download()