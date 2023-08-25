import tkinter as tk    
from tkinter import *
import random
from tkinter import messagebox  

root = tk.Tk()
root.title("rafa gay")
root.geometry('600x600')
root.configure(background='#DCDCDC')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x() <50 and abs(e.y - button_1.winfo_y())) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_width())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo('rafa gay', 'eu sabiakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')

def denied():
    button_1.destroy()

margin = Canvas(root, width=500, bg='#DCDCDC', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg= '#DCDCDC', text='vc é gay?', fg='#000000', font=('montserrat', 24, 'bold'))
text_id.pack()

button_1 =tk.Button(root, text= 'Não', bg='#98FB98', command=denied, relief= RIDGE, bd=3, font=('montserrat', 8, 'bold'))
button_1.pack()

root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='sim', bg='#98FB98', relief= RIDGE, bd=3, command=accepted, font=('montserrant', 8, 'bold'))
button_2.pack()

root.mainloop()







