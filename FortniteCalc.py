#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk


#Variables: Store data about my program
outfitUC = 1
outfitR = 3
outfitE	= 4
outfitL	= 6

pickaxesUC = 3
pickaxesR = 2
pickaxesE = 4
pickaxesL = 2

glidersUC = 10
glidersR = 4
glidersE = 2
glidersL = 3


def clicked1(event):
	#How do I decided who I have clicked on?
	print("Outfits")
	labInput1.config(background = "black", foreground = "white")
	labInput3.config(background = "grey", foreground = "black")
	labInput2.config(background = "grey", foreground = "black")
	labInput6.config(text = "Uncommon Skins: "+str(outfitUC))
	labInput7.config(text = "Rare Skins: "+str(outfitR))
	labInput8.config(text = "Epic Skins: "+str(outfitE))
	labInput8.config(text = "Legendary Skins: "+str(outfitL))

def clicked2(event):
	#How do I decided who I have clicked on?
	print("Pickaxes")
	labInput2.config(background = "black", foreground = "white")
	labInput1.config(background = "grey", foreground = "black")
	labInput3.config(background = "grey", foreground = "black")
	labInput6.config(text = "Uncommon Skins: "+str(pickaxesUC))
	labInput7.config(text = "Rare Skins: "+str(pickaxesR))
	labInput8.config(text = "Epic Skins: "+str(pickaxesE))
	labInput8.config(text = "Legendary Skins: "+str(pickaxesL))

def clicked3(event):
	#How do I decided who I have clicked on?
	print("Gliders")
	labInput3.config(background = "black", foreground = "white")
	labInput2.config(background = "grey", foreground = "black")
	labInput1.config(background = "grey", foreground = "black")
	labInput6.config(text = "Uncommon Skins: "+str(glidersUC))
	labInput7.config(text = "Rare Skins: "+str(glidersR))
	labInput8.config(text = "Epic Skins: "+str(glidersE))
	labInput8.config(text = "Legendary Skins: "+str(glidersL))


root = tk.Tk()









#Three stages to build elements/objects
#1. Construct the Object: We build and configure it.
#2. Configure the Object: We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 9, width = 30) #Parametres are what we send to the function. 
#ordered parametres: the order we send them matters. (COMMON)
#name parametres - JavaScript and Python specific: order doesn't matter but name does
output.config(state = "disable", background = "light blue")
output.grid(row = 0, column = 1, rowspan = 5)

output = tk.Text(root,height = 9, width = 30)
output.config(state = "disable", background = "green")
output.grid(row = 5, column = 1, rowspan = 5)

#Add a section a code that highlights
#the appropriate section - Outfits, Pickaxes or Gliders
#************WIDGET 2,3,4 (Labels)**************
labInput1 = tk.Label(root, text = "Outfits")
labInput1.config(background = "black", foreground = "white")
labInput1.grid(row = 0, column = 0, sticky = "NESW")
labInput1.bind("<Button-1>",clicked1)
labInput1.bind("<Button-2>",clicked1)

labInput2 = tk.Label(root, text = "Pickaxes")
labInput2.config(background = "grey", foreground = "black")
labInput2.grid(row = 1, column = 0, sticky = "NESW")
labInput2.bind("<Button-1>",clicked2)
labInput2.bind("<Button-2>",clicked2)

labInput3 = tk.Label(root, text = "Gliders")
labInput3.config(background = "grey", foreground = "black")
labInput3.grid(row = 2, column = 0, sticky = "NESW")
labInput3.bind("<Button-1>",clicked3)
labInput3.bind("<Button-2>",clicked3)


labInput4 = tk.Label(root, text = "Total = ___", background = "light blue")
labInput4.grid(row = 3, column = 1, sticky = "NESW")

labInput6 = tk.Label(root, text = "Uncommon Skins", background = "light green")
labInput6.grid(row = 5, column = 0, sticky = "NESW")

labInput7 = tk.Label(root, text = "Rare Skins: "+str(outfitR), background = "blue", foreground = "white")
labInput7.grid(row = 6, column = 0,  sticky = "NESW")

labInput8 = tk.Label(root, text = "Epic Skins: ", background = "purple")
labInput8.grid(row = 7, column = 0, sticky = "NESW")

labInput9 = tk.Label(root, text = "Legendary Skins: ", background = "Gold")
labInput9.grid(row = 8, column = 0, sticky = "NESW")

labInput10 = tk.Label(root, text = "Total = ____/100", background = "Green")
labInput10.grid(row = 8, column = 1, sticky = "NESW")

root.mainloop()