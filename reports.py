from tkinter import *
from report1 import report1
from report2 import report2
from report3 import report3
from report4 import report4
from report5 import report5

class reports(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Reports")
        self.geometry("1360x900+0+0")
        self.configure(bg="#dee2ff")
        self.resizable(False, False)

        # labels and buttons
        # frames
        frame = Frame(self, width=700, height=600, bg='#3d5a80')
        frame.place(x=350, y=80)

        # top frame design
        self.heading = Label(frame, text="Reports", font='TimesNewRoman 20 bold', bg='#3d5a80', fg='White')
        self.heading.place(x=250, y=20)

        # button
        self.Button1 = Button(frame, text="Population of Top 30 Countries in the World", command=self.report1, font=("arial", 14, "bold"), bg='#86bbd8', fg='White')
        self.Button1.place(x=130, y=320)

        # button
        self.Button2 = Button(frame, text="Total Share of World's Population in the top 10 countries in 2020", command=self.report2, font=("arial", 14, "bold"), bg='#86bbd8', fg='White')
        self.Button2.place(x=30, y=110)

        # button
        self.Button3 = Button(frame, text="        Top 5 most populated countries in the World        ", command=self.report3, font=("arial", 14, "bold"), bg='#86bbd8', fg='White')
        self.Button3.place(x=80, y=180)

        # button
        self.Button4 = Button(frame, text="Density(P/km.sq.) of the Countries in 2020", command=self.report4,font=("arial", 14, "bold"), bg='#86bbd8', fg='White')
        self.Button4.place(x=140, y=390)

        # button
        self.Button5 = Button(frame, text="Countries having population more than 1 Million", command=self.report5,font=("arial", 14, "bold"), bg='#86bbd8', fg='White')
        self.Button5.place(x=110, y=250)

    def report1(self):
        window = report1()

    def report2(self):
        window = report2()

    def report3(self):
        window = report3()

    def report4(self):
        window = report4()

    def report5(self):
        window = report5()