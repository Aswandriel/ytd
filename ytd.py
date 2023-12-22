import time 
from pytube import YouTube


print("Welcome to ytd!")
print("========================================")
link = input("link to the video that shall be downloaded: ")
place = input("Where do you want to save the video?: ")

yt = YouTube(link)

time.sleep(0.5)

print("Video:\n")
print("title: " + yt.title)
print("length: " + str(yt.length))
print("views: " + str(yt.views))
print("author: " + yt.author)
#print("Caption: " + yt.captions)

con = input("To continue downloading this video press ENTER otherwise pass 'stop'")

if not con == "stop":
    vid = yt.streams.get_by_resolution("720p")

    print("downloading video to " + place)

    vid.download(place)

    print("Download completed!!")




