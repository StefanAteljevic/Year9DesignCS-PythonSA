#This imports the tkinter "Tool box" that contains
#All the support material to make GUI elements.
#by including "as tk"we are giving a short name to use.
import tkinter as tk




root = tk.Tk()
#Three stages to build elements/objects
#1. Construct the object: We build and configure it.
#2. COnfigure the object: We specufy behaviours and settings (OPTIONAL)
#3. Pack the object: Put it in the window
titleLabel = tk.Label(root, text = "Your Daily Running Tracker", font=("Helvetica", 16))
#ordered parameters: The order we send the matters. (COMMON)
#Named parameters: JavaScript and Python specific
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#Widget 2: Text *********************
output = tk.Text(root, height = 10, width = 70,background = "grey", font=("Helvetica", 12))
output.insert(tk.END,"Welcome to your daily running tracker! Before you begin, you need to  input some facts about you.")
output.grid(row = 1, column = 0, columnspan = 2)
#Height = Lines up and down, Width = characters across


#Widget 3: Labels ********************
word1Label = tk.Label(root, text = "Height (Cm)", background = "red", foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = "Weight (Kg)", background = "red", foreground = "blue")
word2Label.grid(row = 6, column = 0, sticky = "NESW")

word3Label = tk.Label(root, text = "Age (Years)", background = "red", foreground = "blue")
word3Label.grid(row = 8, column = 0, sticky = "NESW")

#Widget 4: Entry ***********************
ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 6, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 8, column = 1)

btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 10, column = 1)

root.geometry("500x500")



#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program

