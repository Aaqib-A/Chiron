#Chiron, the eldest and wisest of the centaurs. The ancient trainer of heroes such as Heracles. - Is a centaur.

'''
Modules Install

pip install tktimer
'''


'''
d:
cd Aaqib/Raspberry pi/Projects/Chiron
Chiron_Alpha_0_1.py
'''

#pip install Pillow

# importing whole module 
from tkinter import *
from tkinter.ttk import *
  
# importing strftime function to 
# retrieve system's time 
from time import strftime 
import os

from PIL import ImageTk, Image

bg_color="black"
font_color="white"

# creating tkinter window 
root = Tk() 
root.title('Chiron')
root.configure(bg=bg_color) 
#root.attributes('-fullscreen', True)

# style configuration
style = Style(root)
style.configure('TLabel', background=bg_color)
style.configure('TFrame', background=bg_color)




#=========================== Clock Module ===========================#

clock = Frame(root)
clock.pack(anchor = NE)

#=========================== Clock Module:Image ===========================#

def import_image(image_name, x_size, y_size):
	# opens the image 
	image_path=os.path.join("Images",image_name)
	final_img = Image.open(image_path) 
	# resize the image and apply a high-quality down sampling filter 
	#final_img = final_img.resize((30, 30), Image.ANTIALIAS) 
	final_img = final_img.resize((x_size, y_size)) 
	# PhotoImage class is used to add image to widgets, icons etc 
	final_img = ImageTk.PhotoImage(final_img)
	return final_img
	
moon_img = import_image("Moon.png", 25, 25)
sun_image = import_image("Sun.png", 30, 30)

# create a label 
day_night_image = Label(clock, image = sun_image) 


#=========================== Clock Module:Image ===========================#

  
# This function is used to  
# display time on the label 
clock_refresh_freq = 1000
def time(): 
	curr_day = strftime('%A')
	day_label.config(text = curr_day) 
	
	curr_month = strftime('%B')
	month_label.config(text = curr_month)
	
	curr_time = strftime('%H:%M:%S %p') 
	time_label.config(text = curr_time) 
	
	curr_date = strftime('%d/%m/%Y') 
	date_label.config(text = curr_date) 
	
	if int(strftime('%H')) >= 7 and int(strftime('%H')) <= 18:
		day_night_image.config(image = sun_image) 
	else:
		day_night_image.config(image = moon_img) 
	
	time_label.after(clock_refresh_freq, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
day_label = Label(clock, font = ('calibri', 60, 'bold'), 
            foreground = font_color) 
			
month_label = Label(clock, font = ('calibri', 20, 'bold'), 
            foreground = font_color) 			

time_label = Label(clock, font = ('calibri', 30, 'bold'), 
            foreground = font_color) 
			
date_label = Label(clock, font = ('calibri', 10, 'bold'), 
            foreground = font_color) 

# Placing clock 
day_label.grid(row = 0, columnspan = 3)
day_night_image.grid(row = 1, column = 1, sticky=E)
time_label.grid(row = 1, column = 2, sticky=E)
month_label.grid(row = 2, column = 2)
date_label.grid(row = 2, column = 2, sticky=SE)


time() 
#=========================== Clock Module ===========================#


#=========================== Current Program Usage Tracker  ===========================#
import psutil


process_track = Frame(root)
process_track.pack(anchor = SW)

process_label = Label(process_track, font = ('calibri', 10, 'bold'), 
            foreground = font_color) 
			
def p_track():
	process = psutil.Process(os.getpid())
	mem = process.memory_info().rss / float(2 ** 20)
	process_label.config(text = mem)
	
	process_label.after(5000, p_track) 

process_label.grid(row = 0, column = 0)

p_track() 
			
#=========================== Current Program Usage Tracker  ===========================#

#=========================== Timer  ===========================#


#=========================== Timer  ===========================#


mainloop() 