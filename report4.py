from tkinter import *

class report4(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Density(P/km.sq.) of the Countries in 2020")
        self.geometry("1360x700+0+0")
        self.configure(bg="#b7e4c7")
        self.resizable(False, False)


        self.top_image4 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\images\report4.png")
        self.top_image4_label4 = Label(self, image=self.top_image4)
        self.top_image4_label4.place(x=30, y=100)
