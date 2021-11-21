import pyautogui as pi
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time

root = Tk()
root.title('Autoclicker e Spammer')


global darkmode
darkmode = '#232323'


root.config(bg = darkmode)

###     Variabili e liste

geometry_x = '300'
geometry_y = '300'
str_geom_topl = geometry_x+'x'+geometry_y


num_click=tk.StringVar()
spammm = tk.StringVar()
num_spam = IntVar()

testo = 'Scrivi qui dentro il numero di click\n ricorda che sara moltiplicato per 3!'
testo2 = 'Scrivi qui il testo che vorrai far ripetere\n nella casella sotto il numero di volte'


on = PhotoImage(file='assets\on.png')
off = PhotoImage(file='assets\off.png')
impostazioni_dark = PhotoImage(file = 'assets\impostazioni_dark.png')
impostazioni_light = PhotoImage(file = 'assets\impostazioni_light.png')

on_image = on.subsample(1,1)
photoimage = impostazioni_dark.subsample(1,1)


global is_on
is_on = True

global font_choosen
font_choosen = 'Arial'

####         Finestra
window_width = 550
window_height = 245

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)


###          funzioni/comandi

def sel():

    selection = 'hai selezionato '+ str(num_spam.get())
    num = num_spam.get()
    print(num)
    label_test.config(text = selection)

def Enter(event=None):
    n_clk = num_click.get()
    print(n_clk)

    ###            Logica sistema Clicker
    time.sleep(1)
    x = 0
    while x != int(n_clk):
        pi.click(clicks=10, interval=0.05)
        x += 1

def Enter_spammer(event=None):
    spam = spammm.get()
    spam = str(spam)

    num = int(num_spam.get())

    time.sleep(1)
    
    ###             Logica sistema Spammer    
    pi.click()
    for i in range(num):
        pi.write(spam, interval=0.001)
        pi.press('enter')

def Settings():
    top = Toplevel()
    top.geometry(str_geom_topl)
    top.title("Settings")

    #top.resizable(False, False)

    def switch():
        global is_on
        global darkmode

        if is_on:
            on_button.config(image=off)
            darkmode = '#ffffff'
            
            

            # Cambio colore di tutti i widget
            #sfondo
            root.configure(bg=darkmode)

            label_vuoto1.configure(bg=darkmode, fg=darkmode)
            label_vuoto2.configure(bg=darkmode, fg=darkmode)

            R1.configure(bg=darkmode, fg='black')
            R2.configure(bg=darkmode, fg='black')
            R3.configure(bg=darkmode, fg='black')
            R4.configure(bg=darkmode, fg='black')

            text.configure(bg=darkmode, fg='black')
            text2.configure(bg=darkmode, fg='black')
            label_test.configure(bg=darkmode, fg='black')

            impost.configure(bg=darkmode)
            enter.configure(bg='#e1dfd6', fg='black')
            enter2.configure(bg='#e1dfd6', fg='black')

            e_click.configure(bg=darkmode, fg='black')
            e_spam.configure(bg=darkmode, fg='black')
            impost.configure(bg=darkmode, image=impostazioni_light)

            is_on = False

            # widget impostazioni
            top.config(bg=darkmode)
            l2.config(bg=darkmode, fg='black')
            on_button.config(bg=darkmode)
            comandi.config(bg=darkmode, fg='black')
            label_vuoto3.config(bg=darkmode, fg=darkmode)
            
        else:
            on_button.config(image=on)
            darkmode = '#232323'
            

            # Cambio colore di tutti i widget
            #sfondo
            root.configure(bg=darkmode)

            label_vuoto1.configure(bg=darkmode, fg=darkmode)
            label_vuoto2.configure(bg=darkmode, fg=darkmode)

            R1.configure(bg=darkmode, fg='#ffffff')
            R2.configure(bg=darkmode, fg='#ffffff')
            R3.configure(bg=darkmode, fg='#ffffff')
            R4.configure(bg=darkmode, fg='#ffffff')

            text.configure(bg=darkmode, fg='#ffffff')
            text2.configure(bg=darkmode, fg='#ffffff')
            label_test.configure(bg=darkmode, fg='#ffffff')

            impost.configure(bg=darkmode)
            enter.configure(bg='#4e4e4b', fg='black')
            enter2.configure(bg='#4e4e4b', fg='black')

            e_click.configure(bg=darkmode, fg='#ffffff')
            e_spam.configure(bg=darkmode, fg='#ffffff')

            impost.configure(bg=darkmode, image=impostazioni_dark)

            # widget impostazioni
            top.config(bg=darkmode)
            l2.config(bg=darkmode, fg='#ffffff')
            on_button.config(bg=darkmode)
            comandi.config(bg=darkmode, fg='#ffffff')
            label_vuoto3.config(bg=darkmode, fg=darkmode)

            is_on = True
            
    top.config(bg = darkmode)
    
    l2 = Label(top, text = "Darkmode", bg=darkmode, fg='#ffffff', font='Arial', justify='left')
    l2.grid(row=1,column=0)

    label_vuoto3 = Label(top, text='spazio', bg=darkmode, fg=darkmode)
    label_vuoto3.grid(row=3,column=0)
    comandi = Label(top, text='Lista shortcut per far partire i programmi:\nClicker      Enter\nSpammer      Alt sinistro', bg=darkmode, font=font_choosen, fg='#ffffff', justify='left')
    comandi.grid(row=4,column=0)

    on_button = Button(top, image=on_image, bd=0, command=switch, bg=darkmode)
    on_button.grid(row=1,column=7)

def About():
    top = Toplevel()
    top.geometry(str_geom_topl)
    top.title("About")
    l2 = Label(top, text = "This is toplevel window")

    l2.pack()

def Help():
    top = Toplevel()
    top.geometry(str_geom_topl)
    top.title("Help")
    l2 = Label(top, text = "This is toplevel window")

    l2.pack()


###          vari widget
## barra di sinistra
test1 = Label(root, text='test')
test1.grid(row=1,column=0)

separator = ttk.Separator(root,orient='vertical')
separator.grid(row=0,column=1,rowspan=10,sticky='ns')

# pulsante impostazioni

impost = Button(root, image = impostazioni_dark, bg='#232323', bd=0, highlightcolor=darkmode, command=Settings)
impost.grid(row=9,column=0)
# widget clicker
text = Label(root, text=testo, bg=darkmode, fg='#ffffff')
text.grid(row=0,column=2)

e_click = Entry(root, bd=1, textvariable=num_click, fg='#ffffff', bg=darkmode)
e_click.grid(row=1,column=2)

# label vuoti per sistemare design

label_vuoto1 = Label(root, text='testott',bd=0, bg=darkmode, fg='#232323')
label_vuoto1.grid(row=0,column=4)

label_vuoto2 = Label(root, text='testotesto',bd=0, bg=darkmode, fg='#232323')
label_vuoto2.grid(row=1,column=6)


# widget spammer
text2 = Label(root, text=testo2, bg=darkmode, fg='#ffffff')
text2.grid(row=0,column=7)

e_spam = Entry(root, bd=1, textvariable=spammm, fg='#ffffff', bg=darkmode)
e_spam.grid(row=1,column=7,padx=3,pady=3)

R1 = Radiobutton(root, bg=darkmode, fg='#ffffff', text='10 volte', variable=num_spam, value=10, command=sel)
R1.grid(row=3,column=7)

R2 = Radiobutton(root, bg=darkmode, fg='#ffffff', text='20 volte', variable=num_spam, value=20, command=sel)
R2.grid(row=4,column=7)

R3 = Radiobutton(root, bg=darkmode, fg='#ffffff', text='50 volte', variable=num_spam, value=50, command=sel)
R3.grid(row=5,column=7)

R4 = Radiobutton(root, bg=darkmode, fg='#ffffff', text='100 volte', variable=num_spam, value=100, command=sel)
R4.grid(row=6,column=7)

label_test = Label(root, bg=darkmode, fg='#ffffff')
label_test.grid(row=7,column=7)

###      Pulsante clicker
enter=Button(root, text='Enter', command=Enter, bg='#4e4e4b')
enter.grid(row=2,column=2)

root.bind('<Return>', Enter)


###      Pulsante Spammer
enter2=Button(root, text='Enter', command=Enter_spammer, bg='#4e4e4b')
enter2.grid(row=2,column=7)

root.bind('<Alt_L>', Enter_spammer)

root.mainloop()
