from pytube import YouTube
import os

path = YouTube(input("Rnter the youtube video link here : "))
audio = path.streams.filter(only_audio=True).first()

output_file = audio.download(output_path="G:\mp3_downloader_files")
root, ext = os.path.splitext(output_file)
print(root)
filename = root + ".mp3"
os.rename(output_file, filename)

print("File saved.")