import tkinter as tk


def submit(*args):
	#assumption is that ent1 is an integes
	#I want you to try this and if something goes
	#wrong immediatly go to the except
	try:
		var = int(ent1.get())
		list.append(var)
		
	except:
		print("Please enter an integer!")

	ent1.delete(0,tk.END)
	print(list)
list = []
root = tk.Tk()

ent1 = tk.Entry(root)
ent1.pack()

btn1 = tk.Button(root, text = "Submit", command = submit)
btn1.pack()

root.mainloop()