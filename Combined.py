#This imports the tkinter "Tool box" that contains
#All the support material to make GUI elements.
#by including "as tk"we are giving a short name to use.
import tkinter as tk



#Defining certain events.
#4 definitions below are for faded text when clicking on entry boxes
def on_entry_click(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout1(event):
	if ent1.get() == "":
		ent1.insert(0, "Enter height ; i.e 5'7")
		ent1.config(fg = "grey")
		ent1.grid(row = 2, column = 1)

def on_focusout2(event):
	if ent2.get() == "":
		ent2.insert(0, "Enter weight ; i.e 70")
		ent2.config(fg = "grey")
		ent2.grid(row = 6, column = 1)

def on_focusout3(event):
	if ent3.get() == "":
		ent3.insert(0, "Enter age ; i.e 15")
		ent3.config(fg = "grey")
		ent3.grid(row = 8, column = 1)

def change(*args):
	print("running change")
	print()
	print(var.get())
    

####RUN APP 2
#Defining certain events.
#4 definitions below are for faded text when clicking on entry boxes
def on_entry_click2(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout12(event):
	if ent12.get() == "":
		ent12.insert(0, "Enter distance ran ; i.e 10")
		ent12.config(fg = "grey")
		ent12.grid(row = 2, column = 1)

def on_focusout22(event):
	if ent22.get() == "":
		ent22.insert(0, "Enter time of run ; i.e 60")
		ent22.config(fg = "grey")
		ent22.grid(row = 6, column = 1)





root = tk.Tk()
#Three stages to build elements/objects
#1. Construct the object: We build and configure it.
#2. COnfigure the object: We specufy behaviours and settings (OPTIONAL)
#3. Pack the object: Put it in the window
titleLabel = tk.Label(root, text = "Your Daily Running Tracker©", font=("Helvetica", 16))
#ordered parameters: The order we send the matters. (COMMON)
#Named parameters: JavaScript and Python specific
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#Widget 2: Text *********************
output = tk.Text(root, height = 10, width = 70,background = "grey", font=("Helvetica", 16))
output.insert(tk.END,"Welcome to your Daily Running Tracker!! Before you begin, you need to input some facts        about you. This includes your resting heart rate, your weight, and your age. This is so we can   calculate your total calories burned during a run. The formulas used are -                                     Men: Calories Burned = [(Age x 0.2017) — (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969] x Time / 4.184.                                                                                                                          Women: Calories Burned = [(Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022] x Time / 4.184.                                                                                                                                                                                                                                                                                                                                               Have fun running! - Stefan")
output.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW")
#Height = Lines up and down, Width = characters across


#Widget 3: Labels ********************
word1Label = tk.Label(root, text = "Resting heart rate (BPM)", background = "#C50E00", foreground = "white")
word1Label.grid(row = 2, column = 0, sticky = "NESW", padx = 30, pady = 30)

word2Label = tk.Label(root, text = "Weight (Pounds)", background = "#C50E00", foreground = "white")
word2Label.grid(row = 6, column = 0, sticky = "NESW", padx = 30, pady = 30)

word3Label = tk.Label(root, text = "Age (Years)", background = "#C50E00", foreground = "white")
word3Label.grid(row = 8, column = 0, sticky = "NESW", padx = 30, pady = 30)

word4Label = tk.Label(root, text = "Gender", background = "#C50E00", foreground = "white")
word4Label.grid(row = 9, column = 0, sticky = "NESW", padx = 30, pady = 30)

#Widget 4: Checkbox ******************

contrast = tk.IntVar()
check1 = tk.Checkbutton(root, text="High Contrast On/Off", variable=contrast)
check1.grid()

#Widget 5: Entry ***********************

ent1 = tk.Entry(root)
ent1.insert(0, "Enter rhr ; i.e 80")
ent1.bind("<FocusIn>", on_entry_click)
ent1.bind("<FocusOut>", on_focusout1)
ent1.config(fg = "grey")
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.insert(0, "Enter weight ; i.e 140")
ent2.bind("<FocusIn>", on_entry_click)
ent2.bind("<FocusOut>", on_focusout2)
ent2.config(fg = "grey")
ent2.grid(row = 6, column = 1)

ent3 = tk.Entry(root)
ent3.insert(0, "Enter age ; i.e 15")
ent3.bind("<FocusIn>", on_entry_click)
ent3.bind("<FocusOut>", on_focusout3)
ent3.config(fg = "grey")
ent3.grid(row = 8, column = 1)

#Widget 6: Dropsown ********************

OPTIONS = [

	"Male",
	"Female",
	"Other",
]

var = tk.IntVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.grid(row = 9, column = 1, sticky = "NS")

#Widget 6: Input data button ************

btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 10, column = 1)

#Widget 7: Logo ******************** 

logo = tk.PhotoImage(file = "YourDailyRunningTrackerLogo.png")
logoImage = tk.Label(image = logo)
logoImage.config(background = "white")
logoImage.grid(row = 0, column = 0, columnspan = 2)

##************SCREEN 2
#Widget 1: Labels*********************
word1Label2 = tk.Label(root, text = "Distance ran (KM)", background = "#C50E00", foreground = "white")
word1Label2.grid(row = 2, column = 2, sticky = "NESW", padx = 30, pady = 30)

word2Label2 = tk.Label(root, text = "Time of run (Minutes)", background = "#C50E00", foreground = "white")
word2Label2.grid(row = 6, column = 2, sticky = "NESW", padx = 30, pady = 30)

#Widget 2: Entry boxes****************
ent12 = tk.Entry(root)
ent12.insert(0, "Enter distance ran ; i.e 10")
ent12.bind("<FocusIn>", on_entry_click2)
ent12.bind("<FocusOut>", on_focusout12)
ent12.config(fg = "grey")
ent12.grid(row = 2, column = 2)

ent22 = tk.Entry(root)
ent22.insert(0, "Enter time of run ; i.e 60")
ent22.bind("<FocusIn>", on_entry_click2)
ent22.bind("<FocusOut>", on_focusout22)
ent22.config(fg = "grey")
ent22.grid(row = 6, column = 2)

#Widget 3: Text ***********************

output2 = tk.Text(root, height = 3, width = 70,background = "grey", font=("Helvetica", 16))
output2.insert(tk.END,"                                                           Today you ran ___ KM                                                                                                                       Your pace is ___ per KM                                                                                                                     You burned ___ Calories")
output2.grid(row = 11, column = 2, columnspan = 2, sticky = "NESW")

#Widget 4: Logo ***********************
logo2 = tk.PhotoImage(file = "YourDailyRunningTrackerLogo.png")
logoImage2 = tk.Label(image = logo2)
logoImage2.config(background = "white")
logoImage2.grid(row = 0, column = 2, columnspan = 2)

#Widget 5:
btnGo2 = tk.Button(root, text = "Input Data")
btnGo2.grid(row = 7, column = 3)

#Widget 6: Checkbox ******************

contrast2 = tk.IntVar()
check12 = tk.Checkbutton(root, text="High Contrast On/Off", variable=contrast2)
check12.grid()




#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program