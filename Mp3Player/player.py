from tkinter import *
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo
 
window = Tk()
window.title("Tkinter Play Videos in Video Player")
window.geometry("1280x720")
window.configure(bg="purple")
 
 
def open_file():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        global filename
        filename = file.name
        global videoplayer
        videoplayer = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()
 
 
 
def playAgain():
    print(filename)
    videoplayer.play()
 
def StopVideo():
    print(filename)
    videoplayer.stop()
 
def PauseVideo():
    print(filename)
    videoplayer.pause()
    
 

lbl1 = Label(window, text="Tkinter Video Player", bg="orange red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()
 
openbtn = Button(window, text='Open', command=lambda: open_file())
openbtn.pack(side=TOP, pady=2)
 
playbtn = Button(window, text='Play Audio', command=lambda: playAgain())
playbtn.pack(side=TOP, pady=3)
 
stopbtn = Button(window, text='Stop Audio', command=lambda: StopVideo())
stopbtn.pack(side=TOP, padx=4)
 
pausebtn = Button(window, text='Pause Audio', command=lambda: PauseVideo())
pausebtn.pack(side=TOP, padx=5)
 
 
window.mainloop()
