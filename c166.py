from tkinter import*
from tkinter import ImageTk,Image 

root=Tk()
root.title("Working on Canvas Using Functions")
root.geometry("600x600")
img=ImageTk.PhotoImage(Image.open("start.png"))
canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgray")
canvas.pack()
myimage=canvas.create_image(50,50,image=img)
label1=Label(root,text="enter a color:")
label1.place(relx=0.6,rely=0.9,anchor=CENTER)
input1=Entry(root)
input1.place(relx=0.8,rely=0.9,anchor=CENTER)
input1.insert(0,"black")
oldx=50
oldy=50
newx=50
newy=50
direction=""
def draw(direction,oldx,oldy,newx,newy):
    fillcolor=input1.get()
    
root.mainloop()
