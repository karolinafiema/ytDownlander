from pytube import YouTube

link = input("Enter link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)
time = yt.length // 60
print("Length of video in minutes: ", time)
yd = yt.streams.get_highest_resolution()

print("Downloading...")
yd.download('./Yt') # add folder
print("Download completed")

