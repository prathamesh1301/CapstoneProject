import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_window = tk.Tk()
my_window.geometry("700x500")
main_txt = tk.Text(my_window,height=10,width=52)
my_window.title("Autonomous Navigation of robot")
my_font1=('times', 18, 'bold')
image_lab = tk.Label(my_window,text='Upload photo of the grid',width=20,font=my_font1)  
image_lab.grid(row=1,column=1)
spacer1 = tk.Label(my_window, text="")
spacer1.grid(row=2, column=1)
image_addr = ""
image_upload_btn = tk.Button(my_window, text='Upload File', 
   width=20,command = lambda:upload_file())
image_upload_btn .grid(row=3,column=1)

start_point = tk.StringVar()
start_lab= tk.Label(my_window,text='Start Point: ',width=10,font=('times', 11, 'bold'))  
start_lab.grid(row=2,column=2)
start_txt = tk.Entry(my_window,textvariable = start_point,font = my_font1)
start_txt.grid(row=2,column=3)

spacer2 = tk.Label(my_window, text="")
spacer2.grid(row=3, column=2)
spacer3 = tk.Label(my_window, text="")
spacer3.grid(row=4, column=2)

dest_point = tk.StringVar()
dest_lab= tk.Label(my_window,text='End Point: ',width=10,font=('times', 11, 'bold'))  
dest_lab.grid(row=5,column=2)
dest_txt = tk.Entry(my_window,textvariable = dest_point,font = my_font1)
dest_txt.grid(row=5,column=3)

spacer4 = tk.Label(my_window, text="")
spacer4.grid(row=6, column=2)
spacer5 = tk.Label(my_window, text="")
spacer5.grid(row=7, column=2)

velocity_data = tk.StringVar()
velocity_lab= tk.Label(my_window,text='Velocity Data: ',width=10,font=('times', 11, 'bold'))  
velocity_lab.grid(row=8,column=2)
velocity_txt = tk.Entry(my_window,textvariable = velocity_data,font = my_font1)
velocity_txt.grid(row=8,column=3)

spacer6 = tk.Label(my_window, text="")
spacer6.grid(row=8, column=2)
spacer7 = tk.Label(my_window, text="")
spacer7.grid(row=9, column=2)
spacer8 = tk.Label(my_window, text="")
spacer8.grid(row=10, column=2)
spacer9 = tk.Label(my_window, text="")
spacer9.grid(row=11, column=2)

compute_upload_btn = tk.Button(my_window, text='Compute', 
   width=20)
compute_upload_btn .grid(row=12,column=2)

def upload_file():
    global img
    global image_addr
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    image_addr = img
    img_resized=img.resize((300,300)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(my_window,image=img) # using Button 
    b2.grid(row=2,column=1)
    print(type(image_addr))

def compute():
    global start_point
    global dest_point
    global velocity_data
    global start_txt
    global dest_txt
    global velocity_txt
    start_point = double(start_txt.get())
    dest_point = dest_txt.get()
    velocity_data = velocity_txt.get()
    
   
my_window.mainloop()
