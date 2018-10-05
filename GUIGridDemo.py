#tkinter is a module (tool box) that
#Holds code that you can use
#by using as tk we are just shortening the name
import tkinter as tk

#root is a variable that holds the information
#about the main window. That is the window
#with the close, min, max buttons in the top left
#tk.TK() go in the tk tool box and use the function Tk()
root = tk.Tk() 


#If we want to better position the elements we use
#the grid geometry manager, not the pack
ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)



label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)


#sets up your program in an infinite loop waiting for
#the user to do something. This is an EVENT DRIVEN PROGRAM
#This means a function is called when we "do something"
root.mainloop()