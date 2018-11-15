import tkinter as tk


def change(*args):
	print("running change")
	print()

root = tk.Tk()

OPTIONS = [

	"eggs",
	"bunny",
	"chicken",
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()




root.mainloop()
print("End program")