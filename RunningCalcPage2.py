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

#Widget 1: Labels*********************
word1Label = tk.Label(root, text = "Distance ran (KM)", background = "#C50E00", foreground = "white")
word1Label.grid(row = 2, column = 0, sticky = "NESW", padx = 30, pady = 30)

word2Label = tk.Label(root, text = "Time of run (Minutes)", background = "#C50E00", foreground = "white")
word2Label.grid(row = 6, column = 0, sticky = "NESW", padx = 30, pady = 30)

#Widget 2: Entry boxes****************
ent1 = tk.Entry(root)
ent1.insert(0, "Distance ran ; i.e 10")
ent1.bind("<FocusIn>", on_entry_click)
ent1.bind("<FocusOut>", on_focusout1)
ent1.config(fg = "grey")
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.insert(0, "Time of run ; i.e 60")
ent2.bind("<FocusIn>", on_entry_click)
ent2.bind("<FocusOut>", on_focusout2)
ent2.config(fg = "grey")
ent2.grid(row = 6, column = 1)

#Widget 3: Text ***********************

output = tk.Text(root, height = 10, width = 70,background = "grey", font=("Helvetica", 16))
output.insert(tk.END,"Text")
output.grid(row = 11, column = 0, columnspan = 2, sticky = "NESW")

#Widget 4: Logo ***********************
logo = tk.PhotoImage(file = "ABC.png")
logoImage = tk.Label(image = logo)
logoImage.config(background = "white")
logoImage.grid(row = 0, column = 0, columnspan = 2)

#Widget 5:
btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 7, column = 1)





root.mainloop()