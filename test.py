#This imports the tkinter "Tool box" that contains
#All the support material to make GUI elements.
#by including "as tk"we are giving a short name to use.
import tkinter as tk




def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == "Enter your user name...":
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') #Insert blank for user input
       entry.config(fg = "black")
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, "Enter your username...")


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
output.insert(tk.END,"Welcome to your Daily Running Tracker©! Before you begin, you need to input some facts      about you. This includes you height, your weight, and your age. This is so we can calculate       your Total Energy Expenditure (TEE). This value is used to estimate your daily calorie needs.    The TEE for men  = 864 − 9.72 × age + PA × (14.2 × weight + 503 × height)"
output.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW")
#Height = Lines up and down, Width = characters across


#Widget 3: Labels ********************
word1Label = tk.Label(root, text = "Height (Feet)", background = "#C50E00", foreground = "white")
word1Label.grid(row = 2, column = 0, sticky = "NESW", padx = 30, pady = 30)



word2Label = tk.Label(root, text = "Weight (Kg)", background = "#C50E00", foreground = "white")
word2Label.grid(row = 6, column = 0, sticky = "NESW", padx = 30, pady = 30)

word3Label = tk.Label(root, text = "Age (Years)", background = "#C50E00", foreground = "white")
word3Label.grid(row = 8, column = 0, sticky = "NESW", padx = 30, pady = 30)

contrast = tk.IntVar()
check1 = tk.Checkbutton(root, text="High Contrast On/Off", variable=contrast)
check1.grid()

#Widget 4: Entry ***********************

ent1 = tk.Entry(root)
ent1.insert(0, "Enter height ; i.e 5'7")
ent1.bind("<FocusIn>", on_entry_click)
ent1.bind("<FocusOut>", on_focusout)
ent1.config(fg = "grey")
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.insert(0, "Enter weight ; i.e 70")
ent2.bind("<FocusIn>", on_entry_click)
ent2.bind("<FocusOut>", on_focusout)
ent2.config(fg = "grey")
ent2.grid(row = 6, column = 1)

ent3 = tk.Entry(root)
ent3.insert(0, "Enter age ; i.e 15")
ent3.bind("<FocusIn>", on_entry_click)
ent3.bind("<FocusOut>", on_focusout)
ent3.config(fg = "grey")
ent3.grid(row = 8, column = 1)

btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 9, column = 1)





#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program