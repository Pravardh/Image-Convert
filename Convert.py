from PIL import Image,ImageFilter
from tkinter import ttk,Tk,Label,Button,filedialog
import os

def space(times = 1):
	for i in range(times):
		Label(window,text = '').pack()

def convert():
	Input = '*.' +inputBox.get().lower()

	
	filename = filedialog.askopenfilename(
		title = 'Select an image',
		initialdir = './',
		filetypes = [('Images',Input)]
		)

	Name = filename.split('/')
	Name = Name[-1]
	Name = Name.split('.')
	Name = Name[0]

	img = Image.open(filename)

	Output = '.' +outputBox.get().lower()
	Name = Name + Output
	img = img.convert('RGB')
	img.save(os.getcwd() + '\\Converted Images\\'+Name)
	Label(text = 'Finished Conversion!').pack()

window = Tk()
window.geometry('400x300')
window.resizable(False,False)

Label(window, text = "Image Convertor",font = ('Candara',16)).pack()
space()

inputBox = ttk.Combobox(window,values = ['PNG','JPG','JPEG'])
inputBox.pack()
space(2)

outputBox = ttk.Combobox(window,values = ['PNG','JPG','JPEG'])
outputBox.pack()
space(1)

Button(window,text = "Convert",font = ('Candara',16),command = convert).pack()

window.mainloop()
