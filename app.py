import tkinter as tk
import time

class App(tk.Frame):
"""Clock GUI Window"""
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.label = tk.Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=50,y=80)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

root = tk.Tk()
app=App(root)
root.wm_title("Tkinter clock")
root.geometry("200x200")
root.after(1000, app.update_clock)
root.mainloop()
