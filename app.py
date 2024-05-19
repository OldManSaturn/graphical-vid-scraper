from tkinter import *
from tkinter import ttk
import yt_dlp as youtube_dl

def main():
    youtube_video_url = ""
    download_options = {}
    root = Tk()
    root.title("Video Scraping Tool")
    # Add your forms and widgets here
    url_label = ttk.Label(root, text="Enter URL:")
    url_label.pack()
    url_entry = ttk.Entry(root, width=50)
    url_entry.pack()
    submit_button = ttk.Button(root, text="Submit")
    submit_button.pack()
    youtube_video_url = url_entry.get()
    # Rest of your code
    output_label = ttk.Label(root, text="")
    output_label.pack()

    def submit():
        youtube_video_url = url_entry.get()
        output_label.config(text="Generating download for URL: " + youtube_video_url)
        with youtube_dl.YoutubeDL(download_options) as ydl:
            ydl.download([youtube_video_url])

    submit_button.config(command=submit)
    root.mainloop()

if __name__ == "__main__":
    main()
