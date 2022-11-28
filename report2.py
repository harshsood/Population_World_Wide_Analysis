from tkinter import *

class report2(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Total Share of World's Population in the top 10 countries in 2020")
        self.geometry("1360x700+0+0")
        self.configure(bg="#b7e4c7")
        self.resizable(False, False)


        self.top_image2 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\images\report2.png")
        self.top_image1_label2 = Label(self, image=self.top_image2)
        self.top_image1_label2.place(x=30, y=100)
