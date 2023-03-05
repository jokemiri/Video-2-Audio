#importing modules
import moviepy.editor
from tkinter.filedialog import *
from tkinter import *

root=Tk()

root.geometry("350x125")
root.title("Video 2 Audio Converter")
root.configure(bg="#154c79")
heading = Label(root, text="Video 2 Audio" ,bg='#154c79', font=('Verdana 15')).place(x=120, y=20)
sub_heading = Label(root, text="Choose a File ", bg='#154c79').place(x=25, y=25)

#window_icon
window_icon = PhotoImage(file="icon.png")
root.iconphoto(False, window_icon)

logo = PhotoImage(file='logo.png')
logo_label = Label(root, image=logo, bg='#154c79').place(x=10, y=10)

def browse():
    global video
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    pathlab.config(text=video)

def save():
    audio = video.audio
    audio.write_audiofile("sample.mp3")
    Label(root, text="Video Converted into Audio and Saved Successfully", bg='#154c79', font=('Calibri 15')).pack()
    

pathlab = Label(root)
pathlab.pack()

brouwse_button = Button(root,text='BROWSE',command=browse).place(x=200, y=80)
save_button = Button(root,text='SAVE',command=save).place(x=280, y=80)
root.mainloop()