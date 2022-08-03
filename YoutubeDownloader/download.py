# importing the module 
from pytube import YouTube 
  
# where to save 
path = "C://Users//KIIT//Downloads"
  
# link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=o_ILJXLxrRY"    ]
  
for i in link: 
    try: 
        yt = YouTube(i) 
    except: 
        print("Connection Error") 
      
    #choosing filter or video type
    print("Enter 1 for progressive streams") 
    print("Enter 2 for DASH/adaptive streams") 
    print("Enter 3 for mp3 streams") 
    print("Enter 4 for mp4 streams") 
    choice = int(input())

    if(choice == 1):
        mp4files = yt.streams.filter(progressive=True)
    elif(choice == 2):
        mp4files = yt.streams.filter(adaptive=True)
    elif(choice == 3):
        mp4files = yt.streams.filter(only_audio=True)
    elif(choice == 4):
        mp4files = yt.streams.filter(file_extension='mp4')

    # downloading the video 
    try:
        stream = yt.streams.get_by_itag(22)
        stream.download(path)
        print(f"Video {i} downloading")
    except: 
        print(f"Error video {i} could not be downloaded") 
print("Task Completed") 