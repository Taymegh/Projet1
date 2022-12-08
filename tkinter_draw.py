from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import turtle
#import tools
from PIL import Image, ImageTk

root= Tk()
root.title("Drawing")
# path = "C:\\Users\\tmegh\\Desktop\\IMPORTANT\\Site SAE14"
# load = Image.open(path)
# render = ImageTk.PhotoImage(load)
# root.iconphoto(False, render)




app_height= 600
app_width= 800

screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

x= (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# text= Label(root, text= f'Width: {screen_width} Height: {screen_height}')
# text.pack()


# root.geometry(f'{yes}x{no}+{}+{}')
# root.eval('tk::PlaceWindow . center')
root.config(bg="Grey")


canvas= Canvas(root, width=770, height=400)
canvas.grid(row=0, columnspan=6, padx=10, pady=20)

# filename=PhotoImage(file="Lavisan.png")
# background_label=Label(canvas,image=filename)
# background_label.place(x=0,y=0,relwidth=1,relheight=1)


samuel= turtle.RawTurtle(canvas)
samuel.color("red")
samuel.speed(10)
samuel.up()
samuel.goto(-350,0)
samuel.down()



# color_btn= ttk.Button(root, text= "Color")
# drop= OptionMenu(root, color_btn, "Red", "Blue", "Yellow", "Green")
# drop.pack()
# color_btn.grid(row=1, column=1)
"""
#def open_text():
   text_file = open("test.txt", "r")
   content = text_file.read()
   my_text_box.insert(END, content)
   text_file.close()
"""
"""
def save_text():
   text_file = open("test.txt", "w")
   text_file.write(my_text_box.get(1.0, END))
   text_file.close()
"""
# my_text_box = Text(root, height=10, width=40)
# my_text_box.pack()

# open_btn = Button(root, text="Open Text File", command=open_text)
# open_btn.pack()

# save = Button(root, text="Save File", command=save_text)
# save.pack()
def change_color():
   turtle.color("red")

# l= Label(root, text="Yes")
# l.pack()

# e= Entry(root)
# e.pack()

# b= Button(root, text="Click me")
# b.pack()
myvar = StringVar()
myvar2 = StringVar()




# ----------------------- LETTERS ----------------------------
def l():
    # antonin.hideturtle()
    samuel.left(90)
    samuel.forward(100)
    samuel.left(180)
    samuel.forward(100)
    samuel.left(90)
    samuel.forward(50)
    #move to next letter
    samuel.up()
    samuel.forward(30)
    samuel.down()


def a():
    # antonin.hideturtle()
    samuel.left(75)
    samuel.forward(100)
    samuel.right(150)
    samuel.forward(100)
    samuel.left(180)
    samuel.forward(50)
    samuel.left(75)
    samuel.forward(25)
    #move to next letter
    samuel.up()
    samuel.right(180)
    samuel.forward(50)
    samuel.right(75)
    samuel.forward(50)
    samuel.left(75)
    samuel.down()

def v():
    # antonin.hideturtle()
    samuel.up()
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.right(75)
    samuel.down()
    samuel.forward(105)
    samuel.left(150)
    samuel.forward(105)
    #go to next letter
    samuel.right(75)
    samuel.up()
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()

def i():
    samuel.forward(65)
    samuel.right(180)
    samuel.forward(32.5)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.forward(32.50)
    samuel.right(180)
    samuel.forward(65)
    #go to next letter
    samuel.up()
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()
    


def s():
    samuel.circle(25, extent=160)
    samuel.circle(-25, extent= 160)
    #go to next letter
    samuel.up()
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.forward(20)
    samuel.down()



def n():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(160)
    samuel.forward(110)
    samuel.left(160)
    samuel.forward(105)
    #go to next letter
    samuel.up()
    samuel.right(90)
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(110)
    samuel.left(90)
    samuel.down()

def m():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(140)
    samuel.forward(70)
    samuel.left(100)
    samuel.forward(70)
    samuel.right(140)
    samuel.forward(100)
    #go to next letter
    samuel.up()
    samuel.left(90)
    samuel.forward(30)
    samuel.down()
    

def u():
    samuel.left(90)
    samuel.up()
    samuel.forward(25)
    samuel.down()
    samuel.forward(75)
    samuel.right(180)
    samuel.forward(75)
    samuel.circle(25, 180)
    samuel.forward(75)
    #go to next letter
    samuel.up()
    samuel.right(90)
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()


def e():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.forward(50)
    samuel.left(180)
    samuel.forward(50)
    samuel.right(90)
    samuel.left(180)
    samuel.forward(50)
    samuel.left(90)
    samuel.forward(40)
    samuel.left(180)
    samuel.forward(40)
    samuel.left(90)
    samuel.forward(50)
    samuel.left(90)
    samuel.forward(50)
    #go to next layer 
    samuel.up()
    samuel.forward(30)
    samuel.down()

def t():
    samuel.up()
    # samuel.forward(67.5)
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.down()
    samuel.forward(75)
    samuel.right(180)
    samuel.forward(37.5)
    samuel.left(90)
    samuel.forward(100)
    #go to next letter
    samuel.left(90)
    samuel.up()
    samuel.forward(67.5)
    samuel.down()


def o():
    samuel.up()
    samuel.forward(50)
    samuel.down()
    samuel.circle(50, 360)
    #go to next letter
    samuel.up()
    samuel.forward(80)
    samuel.down()

def b():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.circle(-25, 180)
    samuel.right(180)
    samuel.circle(-25, 180)
    #go to next letter
    samuel.up()
    samuel.right(180)
    samuel.forward(50)
    samuel.down()

def d():
    samuel.left(90)
    samuel.forward(100)
    samuel.left(180)
    samuel.forward(100)
    samuel.left(90)
    samuel.circle(50, 180)
    #go to next letter
    samuel.up()
    samuel.right(180)
    samuel.forward(70)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()


def y_letter():
    samuel.left(90)
    samuel.forward(50)
    samuel.left(30)
    samuel.forward(50)
    samuel.left(180)
    samuel.forward(50)
    samuel.left(120)
    samuel.forward(50)
    #go to next letter
    samuel.up()
    samuel.right(60)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.forward(30)
    samuel.down()

def c():
    samuel.up()
    samuel.forward(40)
    samuel.down()
    samuel.circle(50, extent=-180)
    #go to next later
    samuel.up()
    samuel.right(180)
    samuel.forward(45)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()

def r():
   samuel.left(90)
   samuel.forward(100)
   samuel.right(180)
   samuel.forward(50)
   samuel.left(90)
   samuel.circle(25, extent=180)
   samuel.left(90)
   samuel.forward(55)
   samuel.right(180)
   samuel.right(145)
   samuel.forward(50)
   #go to next letter
   samuel.left(55)
   samuel.up()
   samuel.forward(30)
   samuel.down()

def p():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.circle(-30, 180)
    #go to next layer
    samuel.up()
    samuel.right(180)
    samuel.forward(45)
    samuel.right(90)
    samuel.forward(40)
    samuel.left(90)
    samuel.down()


def w():
    samuel.up()
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.right(75)
    samuel.down()
    samuel.forward(105)
    samuel.left(150)
    samuel.forward(105)
    samuel.right(150)
    samuel.forward(105)
    samuel.left(150)
    samuel.forward(100)
    #go to next letter
    samuel.right(75)
    samuel.up()
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()

def g():
    samuel.up()
    samuel.forward(50)
    samuel.down()
    samuel.circle(50, extent=-180)
    samuel.circle(50, extent=180)
    samuel.left(90)
    samuel.forward(50)
    samuel.left(90)
    samuel.forward(25)
    #go to next letter
    samuel.up()
    samuel.right(180)
    samuel.forward(60)
    samuel.right(90)
    samuel.forward(50)
    samuel.left(90)
    samuel.down()

def j():
    samuel.up()
    samuel.left(90)
    samuel.forward(25)
    samuel.right(180)
    samuel.left(90)
    samuel.down()
    samuel.right(90)
    samuel.circle(15, extent=180)
    samuel.forward(85)
    #go to next letter
    samuel.up()
    samuel.right(90)
    samuel.forward(30)
    samuel.right(90)
    samuel.forward(100)
    samuel.left(90)
    samuel.down()

def k():
    samuel.left(90)
    samuel.forward(100)   
    samuel.right(180)
    samuel.forward(50)
    samuel.left(130)
    samuel.forward(65)
    samuel.right(180)
    samuel.forward(65) 
    samuel.left(90)
    samuel.forward(70) 
    #go to next letter
    samuel.up()
    samuel.left(50)
    samuel.forward(40)
    samuel.down()

def h():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(180)
    samuel.forward(50)
    samuel.left(90)
    samuel.forward(40)
    samuel.left(90)
    samuel.forward(50)
    samuel.right(180)
    samuel.forward(100)
    #go to next letter
    samuel.up()
    samuel.left(90)
    samuel.forward(40)
    samuel.down()

def f():
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.forward(50)
    samuel.right(180)
    samuel.forward(50)
    samuel.left(90)
    samuel.forward(40)
    samuel.right(180)
    samuel.right(90)
    samuel.forward(35)
    #go to next letter
    samuel.up()
    samuel.right(180)
    samuel.forward(35)
    samuel.left(90)
    samuel.forward(60)
    samuel.left(90)
    samuel.forward(80)
    samuel.down()


def z():
    samuel.up()
    samuel.left(90)
    samuel.forward(100)
    samuel.right(90)
    samuel.down()
    samuel.forward(60) 
    samuel.right(130)
    samuel.forward(100)
    samuel.left(130)
    samuel.forward(60) 
    #go to next letter
    samuel.up()
    samuel.forward(40)
    samuel.down()


def x_letter():
    samuel.up()
    samuel.left(90)
    samuel.forward(100)
    samuel.right(150)
    samuel.down()
    samuel.forward(110)
    samuel.up()
    samuel.left(150)
    samuel.forward(95)
    samuel.down()
    samuel.left(150)
    samuel.forward(110)
    #go to next letter
    samuel.up()
    samuel.left(120)
    samuel.forward(95)
    samuel.down()


def q():
    samuel.left(90)
    samuel.circle(-40)
    samuel.left(180)
    samuel.circle(40, 95)
    samuel.forward(20)
    samuel.left(120)
    samuel.forward(40)
    samuel.backward(60)
    #go to next letter
    # antonin.up()
    # antonin.left(130)
    # antonin.forward(100)


# ----------------------- LETTERS ----------------------------

draw = {"a":a, "b":b, "c":c, "l":l, "v":v, "i":i, "s":s, "n":n, "m":m, 
"u": u, "e":e, "t":t, "o":o, "d":d, "y":y_letter, "r": r, "p":p, "w": w, "g":g, "j":j, "k":k, "s":s, "h":h, "f":f, "z":z, "x":x_letter, "q":q}
# for letter in text:
#     if letter in draw.keys():
#         draw[letter]()

L1= Label(text="Enter a color")
L1.place(x=110, y=455)
text_entry = Entry(root, textvariable=myvar, width=20)
text_entry.grid(row=30)
text_entry.place(x= 200,y=450,width=100, height=30)


L2= Label(text="Enter a word")
L2.place(x=510, y=455)
t_entry= Entry(root, textvariable=myvar2, width=20)
t_entry.grid(row=30)
t_entry.place(x= 400,y=450,width=100, height=30)


def clear_canvas():
   samuel.clear()
   samuel.up()
   samuel.goto(-350,0)
   samuel.down()
   # samuel.color(text_entry.get())

def turtle_size(val):
    samuel.pensize(int(val))



L3= Button(text="Clear", command=clear_canvas)
L3.place(x=330, y=455)


slider= Scale(root, from_=1, to=20, orient=HORIZONTAL, command=turtle_size)
slider.place(x=300, y=500)

L4= Label(text="Choose the pensize")
L4.place(x=300, y=550)


def return_pressed(event):
    try:
        if len(text_entry.get()) != 0:
            samuel.color(text_entry.get())
            text_entry.delete(0, END)
    except turtle.TurtleGraphicsError:
        text_entry.delete(0, END)



def print_word(event):
   if len(t_entry.get()) != 0:
      for letter in t_entry.get():
         if letter in draw.keys():
            draw[letter]()
      t_entry.delete(0, END)



text_entry.bind('<Return>', return_pressed)
t_entry.bind('<Return>', print_word)




# canvas.mainloop()
root.mainloop()

