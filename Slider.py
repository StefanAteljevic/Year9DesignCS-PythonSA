import tkinter as tk

root = tk.Tk()
root.title("GUI Slider")

slide1 = tk.Scale(root, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)
slide1.pack()


root.mainloop()