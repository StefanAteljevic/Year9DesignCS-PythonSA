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

#Widget 6: Input data button ************

btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 9, column = 1)

#Widget 7: Logo ******************** 

logo = tk.PhotoImage(file = "ABC.png")
logoImage = tk.Label(image = logo)
logoImage.config(background = "white")
logoImage.grid(row = 0, column = 0, columnspan = 2)



#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program

