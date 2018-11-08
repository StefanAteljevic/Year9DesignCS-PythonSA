import tkinter as tk
import math

def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.config(state="normal")

	outputValue = "Given/nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")

##Input

root = tk.Tk()
root.title("Running Calculator")

#Age, height, and weight homepage.

laba = tk.Label(root, text="Age (Years)")
laba.pack()

enta = tk.Entry(root)
enta.pack()

labh = tk.Label(root, text="Height (Feet)")
labh.pack()

enth = tk.Entry(root)
enth.pack()

labw = tk.Label(root, text="Weight (Pounds)")
labw.pack()

entw = tk.Entry(root)
entw.pack()

btn = tk.Button(root, text="Input Data", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()





