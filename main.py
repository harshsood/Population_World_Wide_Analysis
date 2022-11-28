from tkinter import *
from view_dataset import view_dataset
from reports import reports
from Registration import Registration

class System(object):
    def __init__(self, master):
        self.master = master

        #frame
        f1 = Frame(master, width=1360, height=100, bd=8, bg="#660708")
        f1.place(x=110, y=0)

        lbl_information = Label(f1, font=('arial', 45, 'bold'), text="POPULATION WORLD WIDE ANALYSIS", relief=GROOVE, bd=10, bg="#e5383b", fg="White")
        lbl_information.grid(row=0, column=0)

        f2 = Frame(master, width=1360, height=50, bd=8, bg="#660708")
        f2.place(x=0, y=110)

        self.Button2 = Button(f2, text="View Dataset", command=self.view_dataset, font=("arial", 14, "bold"), bg='#e5383b', fg='White')
        self.Button2.place(x=1080, y=0)

        self.Button2 = Button(f2, text="Reports", command=self.reports, font=("arial", 14, "bold"), bg='#e5383b', fg='White')
        self.Button2.place(x=980, y=0)

        self.Button4 = Button(f2, text="Home", font=("arial", 14, "bold"), bg='#e5383b', fg='White', command=master.destroy)
        self.Button4.place(x=20, y=0)

        self.Button5 = Button(f2, text="Register", font=("arial", 14, "bold"), bg='#e5383b', fg='White', command=self.register)
        self.Button5.place(x=110, y=0)

        #f3 = Frame(master, width=1200, height=450, bd=8, bg="#31572c")
        #f3.place(x=60, y=220)

        self.top_image1 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\homepage_image(2).png")
        self.top_image2_label1 = Label(self.master, image=self.top_image1)
        self.top_image2_label1.place(x=200, y=200)

        self.top_image2 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\final_project_population_analysis.py\homepage_image.png")
        self.top_image2_label2 = Label(self.master, image=self.top_image2)
        self.top_image2_label2.place(x=700, y=200)

    def view_dataset(self):
        window = view_dataset()

    def reports(self):
        window = reports()

    def register(self):
        window = Registration()

def main():
    root = Tk()
    sys = System(root)
    root.title("Population World Wide Analysis")
    root.geometry("1360x900+0+0")
    root.configure(bg='#ffddd2')
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()
