from tkinter import *

class report5(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Countries having population more than 1 Million")
        self.geometry("1360x700+0+0")
        self.configure(bg="#b7e4c7")
        self.resizable(False, False)

        self.top_image5 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\images\report5.png")
        self.top_image5_label5 = Label(self, image=self.top_image5)
        self.top_image5_label5.place(x=30, y=100)
