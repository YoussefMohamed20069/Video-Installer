# Import the important packages
from pytube import YouTube
import cv2
import os

# Define the video class
class Video:
    # Initialize the video with the title and channel and url
    def __init__(self, title, channel, url):
        self.title = title
        self.channel = channel
        self.url = url

    # Print out the video infromations
    def __str__(self):
        return f"Video Title: {self.title}\nChannel: {self.channel}\nURL: {self.url}"
    
    # Install video from youtube to the computer
    def install_video(self):
        # Get the video with the url
        video = YouTube(self.url)

        # Get the video streams
        video_streams = video.streams

        # Show the user all the streams
        for stream in video_streams:
            print(stream)

        # Get the video stream itag from the user
        stream_itag = int(input("Put the itag of the video stream: "))

        # Try to get the video stream you want with the itag
        try:
            video_stream = video_streams.get_by_itag(stream_itag)

            # Get the path you want to install the video in
            path = input("Put the path you want to install the video in: ")

            # Try to install the video
            try:
                installed_videos = video_stream.download(path)

                # Show the user that the download is done
                print("Done")

                # Return the video path
                return path
            except:
                print("Cannot find the video path")
        except:
            print("Cannot Find the stream")

# Define the function that will get the video url
def get_url():
    # Get the video url
    url = input("Put the video url: ")

    # Return the url to use it
    return url

def get_video(url):
    # Get the video with the url
    yt = YouTube(url)

    # Get the video information
    title = yt.title
    channel = yt.author

    # Define the video object
    video = Video(title, channel, url)

    # Print the video informations to the user
    print(video)

    # Check if the user want to install the video or not
    install = input("Do you want to install the video [y/n]: ")

    # If the user want to install the video then install it
    if install.lower() == 'y':
        # Install the video and get the path that it's saved in
        path = video.install_video()
    
    # Exit the program if the user doesn't want to install the video
    elif install.lower() == 'n':
        print("See you later!")
    
    # Exit the program if the user put an invalid input
    else:
        print("Invalid input")

# Start the program
if __name__ == "__main__":
    # Start the get video function
    get_video(get_url())

