from tkinter import *

class report1(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Population of Top 30 Countries in the World")
        self.geometry("1360x700+0+0")
        self.configure(bg="#b7e4c7")
        self.resizable(False, False)


        self.top_image1 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\images\report1.png")
        self.top_image1_label1 = Label(self, image=self.top_image1)
        self.top_image1_label1.place(x=30, y=100)
