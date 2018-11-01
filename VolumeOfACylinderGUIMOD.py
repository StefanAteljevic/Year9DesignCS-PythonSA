import tkinter as tk
import math

#You are writing what. is called an event driven program
#An event driven program is one that sets up some GUI and
#then waits for you to do something, press a button, change an element
#
def submit(*args):

	print("Submit pressed")
	r = float(slide1.get())
	h = float(slide2.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.config(state="normal")
	outputValue = "Given\nradius: "+str(r)+" units\nheight: "+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")



root =tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

slide1 = tk.Scale(root, from_=0, to=100, resolution=0.25, orient=tk.HORIZONTAL, command = submit)
slide1.pack()

labh = tk.Label(root, text="height")
labh.pack()

slide2 = tk.Scale(root, from_=0, to=100, resolution=0.25, orient=tk.HORIZONTAL, command = submit)
slide2.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()





root.mainloop()