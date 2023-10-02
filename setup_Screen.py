#SetUp-Screen
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
mixer.init()

class musicPlayer:
    def __init__(self,Tk):
        self.root = Tk
        self.root.title("Music Player")
        self.root.geometry("700x400")
        self.root.configure(background="grey")
        self.root.resizable(0, 0)        
        #Adding Labels
        self.label=Label(text="Lets Make It", bg="grey",fg="white",font=22).place(x=50,y=20)

        #Adding Images
        self.photo= ImageTk.PhotoImage(file="C://Users//user//Desktop//Python//CodeClause//NewMusicPlayer//bg.jpg")
        photo=Label(self.root,image=self.photo).place(x=50,y=50)


        
        #Label ----
        self.label1=Label(self.root, text="Lets Play It! ", font=19)
        self.label1.pack(side=BOTTOM,fill=X)
        

        #    OPEN FILE
        def OpenFile():
            global filename
            filename=filedialog.askopenfilename()

        #    MENU
        self.menubar=Menu(self.root)
        self.root.configure(menu= self.menubar)

        #    SubMenu
        self.submenu=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File",menu=self.submenu)
        self.submenu.add_command(label="Open", command =OpenFile)
        self.submenu.add_command(label="Exit",command=self.root.destroy)

        
        self.submenu2=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit",menu=self.submenu2)
        self.submenu2.add_command(label="Cut")


        def about():
            tkinter.messagebox.showinfo("About Us","Music Player created by Ibrahim....")



        self.submenu2=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About",menu=self.submenu2)
        self.submenu.add_command(label="About",command=about)


        #functions
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1["text"]="Music Playing..."
                except:
                    tkinter.messagebox.showerror("error","File not found, please try again. ")
                    pass
            else:
                mixer.music.unpause()
                self.label1["text"]="Music Unpaused"

        #creating Buttons
        #Play Button---
        self.play=ImageTk.PhotoImage(file="C:/Users/user/Desktop/Python/CodeClause/NewMusicPlayer/play.png")
        play=Button(self.root,image=self.play,bd=0,bg="white", command=playmusic).place(x=50,y=320)

        #function for pause button
        def musicpaused():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1["text"]="Music Paused...."

        #Pause Button---
        self.pause=ImageTk.PhotoImage(file="C:/Users/user/Desktop/Python/CodeClause/NewMusicPlayer/pause.png")
        pause=Button(self.root,image=self.pause,bd=0,bg="white", command=musicpaused).place(x=160,y=320)


        #function for stop button
        def stopmusic():
            mixer.music.stop()
            self.label1["text"]="Music Stopped.."

         #Stop Button---
        self.stop=ImageTk.PhotoImage(file="C:/Users/user/Desktop/Python/CodeClause/NewMusicPlayer/stop.png")
        stop=Button(self.root,image=self.stop,bd=0,bg="white", command=stopmusic).place(x=270,y=320)



        #function for volume bar---
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)



        #volume bar---
        self.scale=Scale(self.root,from_=0, to=100,orient=HORIZONTAL,bg="dark grey",fg="black",length=150,command=volume)
        self.scale.set(25)
        self.scale.place(x=380,y=322)




root=Tk()
obj= musicPlayer(root)
root.mainloop()