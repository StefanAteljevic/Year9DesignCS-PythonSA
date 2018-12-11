#This imports the tkinter "Tool box" that contains
#All the support material to make GUI elements.
#by including "as tk"we are giving a short name to use.
import tkinter as tk
import math



#Defining certain events.
#4 definitions below are for faded text when clicking on entry boxes
def on_entry_click(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout1(event):
	if ent1.get() == "":
		ent1.insert(0, "Enter rhr ; i.e 80")
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

#Defintion for change

def change(*args):
	print("running change")
	print()
	#print(var.get())

#Definitions for the contrast and font buttons

def changeStateContrast(*args):
	print("Changed Contrast")
	print(var1.get())
	if var1.get() == 1:
		root.config(bg = "black")
		check1.config(bg = "black", fg = "yellow")
		check2.config(bg = "black", fg = "yellow")
	if var1.get() == 0:
		root.config(bg = "#D4796A")
		check1.config(bg = "white",fg = "black")
		check2.config(bg = "white",fg = "black")

def changeStateFont(*args):
	print("Changed Font")
	print(var1.get())
	if var2.get() == 1:
		check1.config(font=("Courier", 44))
		check2.config(font=("Courier", 44))

	if var2.get() == 0:
		check1.config(font=("Courier", 20))
		check2.config(font=("Courier", 20))


#*** Definitions for faded text

def on_entry_click2(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout4(event):
	if ent1.get() == "":
		ent1.insert(0, "Enter distance ran ; i.e 10")
		ent1.config(fg = "grey")
		ent1.grid(row = 2, column = 1)

def on_focusout5(event):
	if ent2.get() == "":
		ent2.insert(0, "Enter time of run ; i.e 60")
		ent2.config(fg = "grey")
		ent2.grid(row = 6, column = 1)

def changeStateContrast2(*args):
	print("Changed Contrast")
	print(var1.get())
	if var1.get() == 1:
		root.config(bg = "black")
		check1.config(bg = "black", fg = "yellow")
		check2.config(bg = "black", fg = "yellow")
	if var1.get() == 0:
		root.config(bg = "white")
		check1.config(bg = "white",fg = "black")
		check2.config(bg = "white",fg = "black")

def changeStateFont2(*args):
	print("Changed Font")
	print(var1.get())
	if var2.get() == 1:
		check1.config(font=("Courier", 44))
		check2.config(font=("Courier", 44))

	if var2.get() == 0:
		check1.config(font=("Courier", 20))
		check2.config(font=("Courier", 20))

#Definition for the submit button

def submit(*args):
	#assumption is that ent1 is an integes
	#I want you to try this and if something goes
	#wrong immediatly go to the except
	print(btnGo["text"])
	if btnGo["text"] == "Input Data":
		try:
			var1 = int(ent1.get())
			print("*")
			var2 = int(ent2.get())
			print("**")
			var3 = int(ent3.get())
			print("***")
			var4 = var.get()
			print("****")
			

			plist.append(var1)
			plist.append(var2)
			plist.append(var3)
			plist.append(var4)
			
					



		except:
			print("ERROR")

		ent1.config(state = "disabled")
		ent2.config(state = "disabled")
		ent3.config(state = "disabled")
		dropDownMenu.config(state = "disabled")
		btnGo.config(text = "Update Information")
		btnGo2.config(state = "normal")
	else:

		ent1.config(state = "normal")
		ent2.config(state = "normal")
		ent3.config(state = "normal")
		dropDownMenu.config(state = "normal")
		btnGo.config(text = "Input Data")
		#delete plist
		while (len(plist) > 0):
			plist.pop()
	#ent1.delete(0,tk.END)
	print(plist)

def submit2(*args):
	print(btnGo2["text"])
	if btnGo2["text"] == "Input Info":
		try: 
			var5 = int(ent4.get())
			print("*")
			var6 = int(ent5.get())
			print("**")

			dlist.append(var5)
			dlist.append(var6)
		except:
			print("bad data")


	#Update output 2
	cb = 0 #store calories burned

	if plist[3] == "Male":
		cb = (plist[2]*0.2017 - plist[1] * 0.09036 + plist[0] * 0.6309 - 55.0969 * dlist[1])/4.184
	output2.config(state = "normal")
	output2.delete("1.0",tk.END)
	output2.insert("1.0","You have burned: "+str(cb)+" calories")
	output2.config(state = "disabled")

	if plist[3] == "Female":
		cb = (plist[2]*0.074 - plist[1] * 0.05741 + plist[0] * 0.4472 - 20.4022 * dlist[1]/4.184
	output2.config(state = "normal")
	output2.delete("1.0",tk.END)
	output2.insert("1.0","You have burned:  "+str(cb)+" calories")
	output2.config(state = "disabled")
	
	print(dlist)



	




plist = []
dlist = []


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
output.config(state = "disabled")

output2 = tk.Text(root, height = 3, width = 70,background = "grey", font=("Helvetica", 16))
output2.grid(row = 8, column = 2, columnspan = 2, sticky = "NESW")
output2.config(state = "disabled")
#Height = Lines up and down, Width = characters across


#Widget 3: Labels ********************
word1Label = tk.Label(root, text = "Resting heart rate (BPM)", background = "#C50E00", foreground = "white")
word1Label.grid(row = 2, column = 0, sticky = "NESW", padx = 30, pady = 30)

word2Label = tk.Label(root, text = "Weight (Pounds)", background = "#C50E00", foreground = "white")
word2Label.grid(row = 6, column = 0, sticky = "NESW", padx = 30, pady = 30)

word3Label = tk.Label(root, text = "Age (Years)", background = "#C50E00", foreground = "white")
word3Label.grid(row = 7, column = 0, sticky = "NESW", padx = 30, pady = 30)

word4Label = tk.Label(root, text = "Gender", background = "#C50E00", foreground = "white")
word4Label.grid(row = 8, column = 0, sticky = "NESW", padx = 30, pady = 30)

#***

word5Label = tk.Label(root, text = "Distance ran (KM)", background = "#C50E00", foreground = "white")
word5Label.grid(row = 2, column = 2, sticky = "NESW", padx = 30, pady = 30)

word6Label = tk.Label(root, text = "Time of run (Minutes)", background = "#C50E00", foreground = "white")
word6Label.grid(row = 6, column = 2, sticky = "NESW", padx = 30, pady = 30)

#Widget 4: Checkbox ******************
var1 = tk.IntVar()
contrast = tk.IntVar()

check1 = tk.Checkbutton(root, text="High Contrast On/Off", variable=var1)
check1.config(font=("Courier", 16))
check1.grid()
var1.trace("w",changeStateContrast)


var2 = tk.IntVar()

check2 = tk.Checkbutton(root, text="Large Font", variable=var2)
check2.config(font=("Courier", 16))
check2.grid()
var2.trace("w",changeStateFont)

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
ent3.grid(row = 7, column = 1)

#***

ent4 = tk.Entry(root)
ent4.insert(0, "Enter distance ran ; i.e 10")
ent4.bind("<FocusIn>", on_entry_click2)
ent4.bind("<FocusOut>", on_focusout4)
ent4.config(fg = "grey")
ent4.grid(row = 2, column = 3)

ent5 = tk.Entry(root)
ent5.insert(0, "Enter time of run ; i.e 60")
ent5.bind("<FocusIn>", on_entry_click2)
ent5.bind("<FocusOut>", on_focusout5)
ent5.config(fg = "grey")
ent5.grid(row = 6, column = 3)

#Widget 6: Dropsown ********************

OPTIONS = [

	"Male",
	"Female",
	"Other",
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.configure(background = "#D4796A")
dropDownMenu.grid(row = 8, column = 1, sticky = "NS")

#Widget 6: Input data button ************

btnGo = tk.Button(root, text = "Input Data", command = submit)
btnGo.grid(row = 10, column = 1)

#***

btnGo2 = tk.Button(root, text = "Input Info", command = submit2)
btnGo2.config(state = "disabled")
btnGo2.grid(row = 7, column = 2)

#Widget 7: Logo ******************** 

logo = tk.PhotoImage(file = "YourDailyRunningTrackerLogo.png")
logoImage = tk.Label(image = logo)
logoImage.config(background = "white")
logoImage.grid(row = 0, column = 2, columnspan = 2)

#***

logo2 = tk.PhotoImage(file = "YourDailyRunningTrackerLogo.png")
logoImage2 = tk.Label(image = logo)
logoImage2.config(background = "white")
logoImage2.grid(row = 0, column = 0, columnspan = 2)

#Colours ***************************

root.configure(background = "#D4796A")

#Process ***************************





#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program