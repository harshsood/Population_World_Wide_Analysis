from tkinter import *

class report3(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Top 5 most populated countries in the World")
        self.geometry("1360x700+0+0")
        self.configure(bg="#b7e4c7")
        self.resizable(False, False)

        self.top_image3 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\images\report3.png")
        self.top_image3_label3 = Label(self, image=self.top_image3)
        self.top_image3_label3.place(x=30, y=100)
