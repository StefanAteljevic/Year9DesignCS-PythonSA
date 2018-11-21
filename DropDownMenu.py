import tkinter as tk


def change(*args):
	print("running change")
	print()
	print(var.get())

root = tk.Tk()

OPTIONS = [

	128,
	129,
	130,
]

var = tk.IntVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()




root.mainloop()
print("End program")