#YOUTUBE VIDEO DOWNLOAD 

#importing libraries
from tkinter import *
from pytube import YouTube

#Display Window
root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")
Label(root,text='Youtube Video Downloader', font='arial 25 bold').pack()

#Link Field
link= StringVar()

Label(root,text='Paste Link Here!', font='arial 15 bold italic').place(x=160, y=60)
link_enter= Entry(root, width=70, textvariable=link).place(x=32, y=90)

#Download Function
def Downloader():
	url = YouTube(str(link.get()))
	video = url.streams.first()
	video.download()

	Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg = '#03bafc', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()

